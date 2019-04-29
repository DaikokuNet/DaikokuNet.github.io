#!/usr/local/bin/perl

# ----------------------------------------------------------------------------------
# Page Counter Version 1.10�i�J�E���g�p�j
#
# Script written by Nishiyama(CGI�_�E�����[�h)
# This script is free
# HomePage http://www.cgi-down.com/
# E-Mail webmaster@cgi-down.com
# (1999/10/22-2000/08/28)
# ���ϗ���
#
# 2000-08-28 V1.10 �^�C�g���F���w�肵�Ă��F���ς��Ȃ��o�O�C���A���b�N�@�\�ǉ��B
# 1999-10-23 V1.00 ���������[�X
#
# �Ĕz�z�֎~�i���p�K������ǂ݉������j
# �g�p���ꂽ�烁�[��������������ƌ��h�ł��B
# �ݒu���s���ȓ_�́A�T�|�[�g�f���ւ��肢���܂��B
# ----------------------------------------------------------------------------------
#
# **********************************************************************************
#                       �I�v�V�����ݒ�@����������
# **********************************************************************************
# -------------------------------------------------------
#      �t�@�C���֘A�ݒ�@���K�{
# -------------------------------------------------------

$jcode    = './jcode.pl';                   # jcode.pl�̈ʒu
$datefile = './dat/pagecon.dat';                # �f�[�^�[�L�^�t�@�C��
$lock     = '1';                            # ���b�N�@�\(1:�g�p����@�@0:�g�p���Ȃ�)
$lockfile = './lock/pagecon.lock';          # ���b�N�t�@�C����(�K�v�ȊO�ύX���Ȃ��ŉ�����)

# **********************************************************************************
#                     �I�v�V�����ݒ�I���@�������܂�
# ----------------------------------------------------------------------------------
# ����ȍ~��������������ꍇ�́A�l�̐ӔC�ōs���ĉ������B
# **********************************************************************************
# [���C������]
if (!(-r $jcode)) { &error(bat_jcode); }
require $jcode;
&read_form;
@DATE = &read_file($datefile);
&registry;

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [�t�@�C���ɋL�^]
sub registry {
  $n_page = $FORM{'page'};
  $n_name = $FORM{'name'};

# IP�A�h���X���擾
  $n_addr = $ENV{'REMOTE_ADDR'};

# ���ݎ��Ԃ̎擾
  ($new_date) = &time;

  $m = 0;
  foreach $lines (@DATE) {
    local($date,$page,$name,$count,$addr) = split(/��|��/,$lines);
    if ($n_name eq $name) {
      $m = 1;
      $count++;
      $lines = "$new_date��$n_page��$n_name��$count��$n_addr��\n";
    }
    push(@NEW,$lines);
  }

# �����̏ꍇ
  if ($lock) {
    foreach $i ( 1, 2, 3, 4, 5, 6 ) {
      if (mkdir("$lockfile", 0755)) {
        last;
      } elsif ($i == 1) {
        local($mtime) = (stat($lockfile))[9];
        if ($mtime < time() - 600) {
          rmdir($lockfile);
        }
      } elsif ($i < 6) {
        sleep(1);
      } else {
        &error(28);   # 6�b�҂��Ă����b�N����Ă���΍��G��
      }
    }
  }
  if ($m == 1) {
    if (!open(OUT, ">$datefile")) { &error(bat_file); }
    print OUT @NEW;
    close (OUT);
  }

# �V�K�̏ꍇ
  elsif ($m == 0) {
    if (!open(OUT, ">>$datefile")) { &error(bat_file); }
    $count = 1;
    print OUT "$new_date��$n_page��$n_name��$count��$n_addr��\n";
    close (OUT);
  }
  if ($lock) {
    rmdir($lockfile);   # �������݂��I����ă��b�N����
  }
  print "Location: $n_page\n\n";
}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [�L�^�t�@�C���̓ǂݍ���]
sub read_file {
  local($date_file) = $_[0];
  if (!open(IN,$date_file)) { &error(bat_file); }
  local(@date_files) = <IN>;
  close(IN);
  return @date_files;
}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [�t�H�[���f�[�^���擾���A�����R�[�h����]
sub read_form {
  local($pair,$form_date);
  if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $form_date, $ENV{'CONTENT_LENGTH'}); }
  else { $form_date = $ENV{'QUERY_STRING'}; }
  local(@pairs) = split(/&/,$form_date);
  foreach $pair (@pairs) {
    local($name,$value) = split(/=/,$pair);
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/eg;
    $value =~ s/"/&quot\;/g;
    $value =~ s/<>/&gt\;&lt\;/g;
    &jcode'convert(*value,'sjis');
    $FORM{$name} = $value;
  }
}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [���ݎ������擾]
sub time{
  $ENV{'TZ'} = "JST-9";
  ($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime();
  $year = $year + 1900;
  $mon = sprintf("%.2d",$mon +1);
  $mday = sprintf("%.2d",$mday);
  $hour = sprintf("%.2d",$hour);
  $min = sprintf("%.2d",$min);
  $sec = sprintf("%.2d",$sec);
# �j������{�ꉻ
  @week = ('��','��','��','��','��','��','�y');
  $wday = $week[$wday];
  local($date) = "$year�N$mon��$mday��($wday) $hour��$min��$sec�b";
  return ($date);
}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [�G���[�֘A]
sub error {
  $error = $_[0];
  if ($error eq "bat_jcode") { $error_message = 'jcode.pl ��������܂���'; }
  elsif ($error eq "bat_code") { $error_message = '�T�|�[�g����Ă��Ȃ������R�[�h�ł�'; }
  elsif ($error eq "bat_file") { $error_message = '�f�[�^�t�@�C��������܂���'; }

  print "Content-type: text/html\n\n";
  print "<html><head><title>$error_message</title></head>\n";
  print "<BODY bgcolor=ffffff text=000000>\n";
  print "<BR><BR><BR><CENTER>\n\n";
  print "<TABLE BORDER=0>\n";
  print "<TR><TD BGCOLOR=#FFCCCC WIDTH=70 ALIGN=center>\n";
  print "<FONT SIZE=4><B>�G���[</B></FONT></TD>\n\n";
  print "<TD BGCOLOR=#FFCC99 WIDTH=500 ALIGN=center>\n";
  print "<FONT SIZE=4><B>$error_message</B></FONT></TD></TR>\n";
  print "</CENTER>\n\n";
  print "</BODY></HTML>\n";
  exit;
}
