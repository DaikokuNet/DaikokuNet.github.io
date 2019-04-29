#!/usr/local/bin/perl

# ----------------------------------------------------------------------------------
# Page Counter View Version 1.10�i�J�E���g�\���p�j
#
# Script written by Nishiyama(CGI�_�E�����[�h)
# This script is free
# HomePage http://www.cgi-down.com/
# E-Mail webmaster@cgi-down.com
# (1999/10/22-2000/08/28)
# ���ϗ���
#
# 2000-08-28 V1.10 �^�C�g���F���w�肵�Ă��F���ς��Ȃ��o�O�C���B���b�N�@�\�ǉ��B
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
#      �Ǘ��҂̐ݒ�i�Ǘ��҂Ƃ́A���Ȃ��ł��j���K�{
# -------------------------------------------------------

$master_name = 'user';            # �Ǘ��҂̖��O
$master_email = 'user@**.ne.jp';  # �Ǘ��l�̃��[���A�h���X
$master_pass = 'abc';             # �Ǘ��l�̃p�X���[�h
$master_url = 'http://www....';   # �Ǘ��҂�URL�i�g�b�v�y�[�W�j

# -------------------------------------------------------
#      �t�@�C���֘A�ݒ�@���K�{
# -------------------------------------------------------

$jcode    = './jcode.pl';         # jcode.pl�̈ʒu
$cgifile  = './pageview.cgi';     # ����CGI�̈ʒu
$datefile = './dat/pagecon.dat';      # �f�[�^�[�L�^�t�@�C��(pagecon.cgi�Ɠ����ɂ���)
$gurafu   = './gurafu.gif';       # �O���t�pGIF�摜�̈ʒu

# -------------------------------------------------------
#      ���̑��K�v�ɉ����Đݒ肷�鍀��
# -------------------------------------------------------

$title ='�l�C�y�[�W';             # �^�C�g��
$size  = '300';                   # �O���t�̃T�C�Y�����߂�W���ł��B
                                  # �O���t�̕������܂�傫���Ȃ肷�����Ƃ��͐��l�����炵�ĉ������B
# ---------- �e�F�ݒ蕔 --------------
$title_color   = '#4682b4';       # ����CGI�̃^�C�g���̕����F
$table_color   = '#E6E6FA';       # �e�[�u���J���[
# ---------- body�F�ݒ蕔 ------------
$background    = '';              # �o�b�N�摜���g�p����Ƃ��́u''�v�̊Ԃ�http://�`
                                  # ���́A���΃p�X�ŉ摜�̈ʒu���������������B
                                  # �g�p���Ȃ��Ƃ��́A���̂܂܂�OK�B

$bgcolor       = '#ffffff';       # �w�i�F(�o�b�N�摜�����g���̏ꍇ�͖����ƂȂ�܂�)
$text_color    = '#000000';       # �ʏ핶���F
$link_color    = '#3366cc';       # LINK�̕����F
$alink_color   = '#ff69b4';       # ALINK�̕����F
$vlink_color   = '#c71585';       # VLINK�̕����F

# **********************************************************************************
#                     �I�v�V�����ݒ�I���@�������܂�
# ----------------------------------------------------------------------------------
# ����ȍ~��������������ꍇ�́A�l�̐ӔC�ōs���ĉ������B
# **********************************************************************************
# [���C������]
if (!(-r $jcode)) { &error(bat_jcode); }
require $jcode;
@DATE = &read_file($datefile);
&read_form;
&html_view;
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [�w�b�_�[����]
sub html_header {
  print "Content-type: text/html\n\n";
  print "<HTML><HEAD><TITLE>$title</TITLE></HEAD>\n";
  if ($background eq '') {
    print "<BODY BGCOLOR=$bgcolor TEXT=$text_color LINK=$link_color ALINK=$alink_color VLINK=$vlink_color>\n";
  } else {
    print "<BODY BACKGROUND=$background BGCOLOR=$bgcolor TEXT=$text_color LINK=$link_color ALINK=$alink_color VLINK=$vlink_color>\n";
  }
  print "<DIV ALIGN=center><FONT SIZE=5 color=\"$title_color\"><B>$title</B></FONT></DIV>\n\n";
  print "<DIV ALIGN=right>���@<A HREF=\"$master_url\" TARGET=\"_top\">HOME</A>�@��</DIV>\n";

  print "<HR>\n\n";
}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [�t�b�^�[����]
sub html_footer {
  print "<DIV ALIGN=right>[�Ǘ��ҁF<A HREF=\"mailto:$master_email\">$master_name</A>]</DIV>\n";
  print "<HR>\n";

## ���쌠�\���i�K���\�����ĉ������j
  print "<DIV ALIGN=right>Page Counter Version 1.10 [<A HREF=\"http://www.cgi-down.com/\">CGI�_�E�����[�h</A>]</DIV>\n";

  print "</BODY></HTML>\n";
}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [�s�n�o�\��]
sub html_view {
  &html_header;

# �A�z�z��ɑ��
  $num = 0;
  foreach $lines (@DATE) {
    local($date,$page,$name,$count,$addr) = split(/��|��/,$lines);
    local($day,$hr) = split(/ /,$date);
    $totle = $totle + $count;
    $num++;
    $day{$num} = $day;
    $page{$num} = $page;
    $name{$num} = $name;
    $count{$num} = $count;
    $addr{$num} = $addr;
  }

  print "<CENTER>\n";
  print "<TABLE BORDER=1 bgcolor=$table_color>\n";
  print "<TR>\n";
  print "<TD ALIGN=center><B>����</B></TD>\n";
  print "<TD ALIGN=center><B>�A�N�Z�X��</B></TD>\n";
  print "<TD ALIGN=center><B>�y�[�W��</B></TD>\n";
  print "<TD ALIGN=center><B>�A�N�Z�X��</B></TD>\n";
  print "<TD ALIGN=center><B>�O���t</B></TD>\n";
  print "</TR>\n\n";

# �_�E�����[�h���̑������ʃ\�[�g���\������B
  $ranking = 0;
  foreach (sort { ($count{$b} <=> $count{$a}) || ($a cmp $b)} keys(%count)) {
    $ranking++;
    $part = int($count{$_} / $totle * $size);
    print "<TR>\n";
    print "<TD ALIGN=right><B>$ranking</B></TD>\n";
    print "<TD ALIGN=right><B>$day{$_}</B></TD>\n";
    print "<TD ALIGN=center><A HREF=\"$page{$_}\"><B>$name{$_}</B></A></TD>\n";
    print "<TD ALIGN=right><B>$count{$_}</B></TD>\n";
    print "<TD ALIGN=left><img src=$gurafu width=$part height=20></TD>\n";
    print "</TR>\n\n";
  }
  print "<TR>\n";
  print "<TD ALIGN=center><B>���v</B></TD>\n";
  print "<TD ALIGN=center><B>�@</B></TD>\n";
  print "<TD ALIGN=center><B>�@</B></TD>\n";
  print "<TD ALIGN=right><B>$totle</B></TD>\n";
  print "<TD ALIGN=center><B>�@</B></TD>\n";
  print "</TR>\n\n";
  print "</TABLE>\n";
  print "</CENTER>\n\n";
  &html_footer;
  exit;
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
    &jcode'convert(*value,'sjis');
    $FORM{$name} = $value;
  }
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
