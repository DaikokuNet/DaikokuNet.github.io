#��������������������������������������������������������������������
#�� Web Forum v4.8 - 2006/08/03
#�� Copyright (c) KentWeb
#�� webmaster@kent-web.com
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
$ver = 'Web Forum v4.8';
#��������������������������������������������������������������������
#��[ ���ӎ��� ]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B
#��������������������������������������������������������������������
#
# [�ݒu��] ���������̓p�[�~�b�V����
#
#    public_html / index.html (�z�[���y�[�W)
#       |
#       +-- bbs / wforum.cgi   [705]
#            |    wf_regi.cgi  [705]
#            |    wf_admin.cgi [705]
#            |    wf_init.cgi  [604]
#            |    wf_log.cgi   [606]
#            |    jcode.pl     [604]
#            |    fold.pl      [604]
#            |    pastno.dat   [606] ... (�ߋ����O�p)
#            |    title.gif
#            |
#            +-- past [707] / 0001.cgi [606] ... (�ߋ����O�p)
#            |
#            +-- lock [707] /

#---------------------------------------
#  ����{�ݒ�
#---------------------------------------

# �f���^�C�g����
$title = "Daikoku-NET Web Forum";

# �^�C�g�������̐F
$t_color = "#004080";

# �^�C�g�������̃T�C�Y
$t_point = '20px';

# �^�C�g���摜���g�p����Ƃ�
$t_img = "./title.gif";
$t_w = 151; 	# ���T�C�Y�i�s�N�Z���j
$t_h = 28;	# �c�T�C�Y�i�s�N�Z���j

# �{���̕����T�C�Y
$b_size = '13px';

# �{���̕����t�H���g
$b_face = 'MS UI Gothic, Osaka, �l�r �o�S�V�b�N';

# �p�X���[�h (���p�p������)
$pass = '41264126';

# �ő�L����
$max = 800;

# �߂��̂t�q�k(index.html�Ȃ�)
$home = "http://www.daikokunet.jp/";

# �ǎ��E�w�i�F�E�����F�Ȃ�
$bg = "";		# �ǎ��̎w�� (http://����L�q)
$bc = "#EEEEEE";	# �w�i�F
$te = "#004080";	# �����F
$li = "#0000FF";	# �����N�F�i���K��j
$vl = "#008080";	# �����N�F�i���K��j
$al = "#DD0000";	# �����N�F�i�K�⒆�j

# �X�N���v�gURL
$script = './wforum.cgi';

# �Ǘ��t�@�C��URL
$admin = './wf_admin.cgi';

# �����t�@�C��URL
$regist = './wf_regi.cgi';

# ���O�t�@�C��
$logfile = './wf_log.cgi';

# ���b�N�t�@�C���@�\
#  0 : �s�Ȃ�Ȃ�
#  1 : �s�Ȃ��isymlink�֐����j
#  2 : �s�Ȃ��imkdir�֐����j
$lockkey = 1;

# ���b�N�t�@�C����
#  �� ���̃f�B���N�g���̃p�[�~�b�V������777�ɂ��邱��
$lockfile = './lock/wforum.lock';

# URL���������N (0=no 1=yes)
$autolink = 1;

# �L���� [�薼] �̐F
$sub_color = "#dd0000";

# �L�����n�̐F�i�ꊇ�\�������j
$tbl_color = "#FFFFFF";

# �L����NEW�}�[�N��t���鎞��
$new_time = 48;

# NEW�}�[�N�̕\���`��
#  �� �摜���g�p����ꍇ�ɂ� $newmark = '<img src="./new.gif">';
#     �Ƃ����悤�� IMG�^�O���L�q���Ă��悢
$newmark = '<font color="#FF3300">new!</font>';

# �L��NO�̐F
$no_color = "#008000";

# �V���L���ꊇ�\���̋L����
$sortcnt = 10;

# �ł�����c���[�\����
$p_tree = 10;

# ���X�g�ɕ\������u�L���^�C�g���v�̍ő咷�i�������F���p�������Z�j
$sub_length = 30;

# ���[���A�h���X�̓��͂�K�{ (0=no 1=yes)
$in_email = 0;

# ���X��������c���[���g�b�v�ֈړ� (0=no 1=yes)
$top_sort = 1;

# ���X�͉����珇�ɕt���� (0=no 1=yes)
$bot_res = 1;

# ���p���F�ύX
#  �� �����ɐF�w����s���Ɓu���p���v��F�ύX���܂�
#  �� ���̋@�\���g�p���Ȃ��ꍇ�͉����L�q���Ȃ��ŉ����� ($refcol="";)
$refcol = "#804000";

# �ʉ�ʂ̏㕔�^�C�g���F�i�V���L���Ȃǁj
$backCol = "#004080";	# ���n�F
$charCol = "#ffffff";	# �����F

# �L���̍X�V�́umethod=POST�v����i�Z�L�����e�B�΍�j
#  0 : no
#  1 : yes
$postonly = 1;

# ���e������ƃ��[���ʒm���� : sendmail�K�{
#  0 : �ʒm���Ȃ�
#  1 : �ʒm����i�����̋L���͑��M���Ȃ��j
#  2 : �ʒm����i�����̋L�������M����j
$mailing = 2;

# ���[���ʒm����ۂ̃��[���A�h���X
$mailto = 'facclog@ybb.ne.jp';

# sendmail�p�X�i���[���ʒm���鎞�j
$sendmail = '/usr/lib/sendmail';

# �c���[�̃w�b�_�[�L��
$treehead = "��";

# �ߋ����O�@�\ (0=no 1=yes)
$pastkey = 1;

# �ߋ����O�J�E���g�t�@�C��
$nofile = './pastno.dat';

# �ߋ����O�̃f�B���N�g���i�Ō�� / �ŕ���)
$pastdir = './past/';

# �ߋ����O�P�y�[�W����̍ő�s��
#  �� ����𒴂���Ǝ����I�Ɏ��t�@�C���𐶐����܂�
$max_line = 650;

# �z�X�g�擾���@
# 0 : gethostbyaddr�֐����g��Ȃ�
# 1 : gethostbyaddr�֐����g��
$gethostbyaddr = 0;

# �A�N�Z�X�����i���p�X�y�[�X�ŋ�؂�A�A�X�^���X�N�j
#  �� ���ۃz�X�g�����L�q�i�����v�j�y��z*.anonymizer.com
$deny_host = '*.ap.yournet.ne.jp *.ap.gmo-access.jp *.o-tokyo.nttpc.ne.jp *.d-osaka.nttpc.ne.jp *.p-osaka.nttpc.ne.jp *marunouchi.tokyo.ocn.ne.jp *osakakita.osaka.ocn.ne.jp';
#  �� ����IP�A�h���X���L�q�i�O����v�j�y��z210.12.345.*
$deny_addr = '49.240.241.168 110.3.96.100 110.3.112.64 126.36.33.113 192.151.156.66 113.230.99.17 122.140.64.200 198.204.226.234 198.204.226.202 123.187.16.8 198.204.226.242  112.252.92.183';

# �֎~���[�h
# �� ���e���֎~���郏�[�h���R���}�ŋ�؂�
$no_wd = 'http://,�j�Ȃ�,�G��,�����,���o�Q,���~,���e,�}��,�f�R���O,�{��,�X�^�[,����Ă�,������,�l��,�����,����,����,���,�����ꂽ��,�v���C,44m4,google,�Z�N���X,���z,�o�b�N,shop,online,www.acneonindiajp';

# ���{��`�F�b�N�i���e�����{�ꂪ�܂܂�Ă��Ȃ���΋��ۂ���j
# 0=No  1=Yes
$jp_wd = 1;

# URL���`�F�b�N
# �� ���e�R�����g���Ɋ܂܂��URL���̍ő�l
$urlnum =0;

# �P�񓖂�̍ő哊�e�T�C�Y (bytes)
$maxData = 51200;

# ���T�C�g���瓊�e�r�����Ɏw�� (http://���珑��)
$baseUrl = '';

# ���e����
#  0 : ���Ȃ�
#  1 : ����IP�A�h���X����̓��e�Ԋu�𐧌�����
#  2 : �S�Ă̓��e�Ԋu�𐧌�����
$regCtl = 1;

# �������e�Ԋu�i�b���j
#  �� $regCtl �ł̓��e�Ԋu
$wait = 600;

#---------------------------------------
#  ���ݒ芮��
#---------------------------------------

#---------------------------------------
#  �t�H�[���f�R�[�h
#---------------------------------------
sub decode {
	$post_flag = 0;
	local($buf);
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		$post_flag = 1;
		if ($ENV{'CONTENT_LENGTH'} > $maxData) {
			&error("���e�ʂ��傫�����܂�");
		}
		read(STDIN, $buf, $ENV{'CONTENT_LENGTH'});
	} else {
		$buf = $ENV{'QUERY_STRING'};
	}
	undef(%in);
	foreach ( split(/&/, $buf) ) {
		local($key, $val) = split(/=/);
		$val =~ tr/+/ /;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;

		# S-JIS�ϊ�
		&jcode'convert(*val, "sjis", "", "z");

		# �^�O����
		$val =~ s/\t//g;
		$val =~ s/&/&amp;/g;
		$val =~ s/</&lt;/g;
		$val =~ s/>/&gt;/g;
		$val =~ s/"/&quot;/g;
		$val =~ s/\r\n/\t/g;
		$val =~ s/\r/\t/g;
		$val =~ s/\n/\t/g;

		$in{$key} .= "\0" if (defined($in{$key}));
		$in{$key} .= $val;
	}
	$mode = $in{'mode'};
	$page = $in{'page'};
	if ($page eq "") { $page = 0; }
	$in{'pastlog'} =~ s/\D//g;

	# �������s
	if (($mode eq "form" && $in{'pview'} ne "on" && $in{'wrap'} eq "hard") || ($mode eq "regist" && $in{'wrap'} eq "hard")) {
		local($tmp);
		while ( length($in{'message'}) ) {
			($folded, $in{'message'}) = &fold($in{'message'}, 64);
			$tmp .= "$folded\t";
		}
		$in{'message'} = $tmp;
	}

	# �R�����g���s�R�[�h����
	while ( $in{'message'} =~ /\t$/ ) { $in{'message'} =~ s/\t$//g; }
	$in{'message'} =~ s/\t/<br>/g;

	# �^�C���]�[������{���Ԃɍ��킹��
	$ENV{'TZ'} = "JST-9";
	$headflag = 0;
	$lockflag = 0;
}

#---------------------------------------
#  ���b�N����
#---------------------------------------
sub lock {
	local($retry) = 5;

	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 30) { &unlock; }
	}
	# symlink�֐������b�N
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	# mkdir�֐������b�N
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error('LOCK is BUSY'); }
			sleep(1);
		}
	}
	$lockflag = 1;
}

#---------------------------------------
#  ���b�N����
#---------------------------------------
sub unlock {
	if ($lockkey == 1) {
		unlink($lockfile);
	} elsif ($lockkey == 2) {
		rmdir($lockfile);
	}

	$lockflag = 0;
}

#---------------------------------------
#  HTML�w�b�_
#---------------------------------------
sub header {
	local($meta) = @_;

	if ($headflag) { return; }
	if ($bg) { $bg = "background=\"$bg\""; }

	print "Content-type: text/html\n\n";
	print <<EOM;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META HTTP-EQUIV="Content-Style-Type" content="text/css">
<STYLE type="text/css">
<!--
body,tr,td,th { font-size:$b_size; font-family:"$b_face"; }
a:hover       { text-decoration:underline; color:$al; }
.num          { font-family:Verdana,Helvetica,Arial; }
.obi          { background-color:$backCol; color:$charCol; }
-->
</STYLE>
EOM

	print "$meta\n" if ($meta);

	print <<EOM;
<title>$title</title></head>
<body bgcolor="$bc" text="$te" link="$li" vlink="$vl" alink="$al" $bg>
EOM
	$headflag = 1;
}

#---------------------------------------
#  �G���[����
#---------------------------------------
sub error {
	&unlock if ($lockflag);

	&header();
	print <<EOM;
<div align="center">
<hr width="400">
<h3>ERROR !</h3>
<font color="#dd0000">$_[0]</font>
<p>
<hr width="400">
<p>
<form>
<input type="button" value="�O��ʂɂ��ǂ�" onclick="history.back()">
</form>
</div>
</body>
</html>
EOM
	exit;
}

#---------------------------------------
#  �A�N�Z�X����
#---------------------------------------
sub axsCheck {
	# IP&�z�X�g�擾
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};

	if ($gethostbyaddr && ($host eq "" || $host eq $addr)) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
	}

	# IP�`�F�b�N
	local($flg);
	foreach ( split(/\s+/, $deny_addr) ) {
		s/\./\\\./g;
		s/\*/\.\*/g;

		if ($addr =~ /^$_/i) { $flg = 1; last; }
	}
	if ($flg) {
		&error("�A�N�Z�X��������Ă��܂���");

	# �z�X�g�`�F�b�N
	} elsif ($host) {

		foreach ( split(/\s+/, $deny_host) ) {
			s/\./\\\./g;
			s/\*/\.\*/g;

			if ($host =~ /$_$/i) { $flg = 1; last; }
		}
		if ($flg) {
			&error("�A�N�Z�X��������Ă��܂���");
		}
	}
	if ($host eq "") { $host = $addr; }
}

#---------------------------------------
#  ���Ԏ擾
#---------------------------------------
sub get_time {
	local($time, $log) = @_;
	local($date);

	$time ||= time ;
	local($min,$hour,$day,$mon,$year,$wday) = (localtime($time))[1..6];

	if ($log eq "log") {
		$date = sprintf("%02d/%02d/%02d-%02d:%02d",
				$year-100,$mon+1,$day,$hour,$min);
	} else {
		@week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
		$date = sprintf("%04d/%02d/%02d(%s) %02d:%02d",
				$year+1900,$mon+1,$day,$week[$wday],$hour,$min);
	}
	$date;
}

#---------------------------------------
#  �z�X�g���擾
#---------------------------------------
sub get_host {
	# IP,�z�X�g�擾
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($gethostbyaddr && ($host eq "" || $host eq $addr)) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2) || $addr;
	}
}

#---------------------------------------
#  ���̓`�F�b�N
#---------------------------------------
sub chk_form {
	local($err);

	# POST����
	if ($postonly && !$post_flag) { &error("�s���ȃA�N�Z�X�ł�"); }

	# ���T�C�g����̃A�N�Z�X��r��
	if ($baseUrl) {
		$baseUrl =~ s/(\W)/\\$1/g;
		local($ref) = $ENV{'HTTP_REFERER'};
		$ref =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2", $1)/eg;
		if ($ref && $ref !~ /$baseUrl/i) { &error("�s���ȃA�N�Z�X�ł�"); }
	}

	# �`�F�b�N
	if ($no_wd) { &no_wd; }
	if ($jp_wd) { &jp_wd; }
	if ($urlnum > 0) { &urlnum; }

	if ($in{'name'} eq "" || $in{'name'} =~ /^(\x81\x40|\s)+$/)
		{ $err .= "���O�̓��̓����ł�<br>"; }
	if ($in{'message'} eq "" || $in{'message'} =~ /^(\x81\x40|\s|<br>)+$/)
		{ $err .= "�R�����g�̓��̓����ł�<br>"; }
	if ($in_email && $in{'email'} !~ /^[\w\.\-]+\@[\w\.\-]+\.[a-zA-Z]{2,5}$/)
		{ $err .= "E-Mail�̓��͂��s���ł�<br>"; }
	if ($in{'sub'} eq "" || $in{'sub'} =~ /^(\x81\x40|\s)+$/)
		{ $err .= "�薼�̓��̓����ł�<br>"; }
	if ($in{'url'} eq "http://") { $in{'url'} = ""; }

	if ($err) { &error($err); }
}

#---------------------------------------
#  ���e�t�H�[����
#---------------------------------------
sub msg_form {
	# �N�b�L�[�擾
	local($cname,$cmail,$curl,$cpwd,$cpv,$csmail) = &get_cookie;
	$curl ||= 'http://';

	# �C����
	if ($_[0] eq "edt") {
		($type,$cname,$cmail,$curl,$csmail,$res_sub,$res_msg,$wrap) = @_;

#		$res_msg =~ s/"/&quot;/g;
		if (!$wrap) { $wrap = 'soft'; }
		print "<form><input type=button value='�O��ʂɖ߂�' onClick='history.back()'></form>\n";
		print "<h3>�C���t�H�[��</h3>\n";
		print "<form action=\"$regist\" method=\"post\">\n";
		print "<input type=hidden name=mode value=\"usr_edt\">\n";
		print "<input type=hidden name=action value=\"edit\">\n";
		print "<input type=hidden name=pwd value=\"$in{'pwd'}\">\n";
		print "<input type=hidden name=no value=\"$in{'no'}\">\n";
	# �ԐM��
	} elsif ($mode eq 'msgview') {
		$wrap='soft';
		print "<hr width=\"95%\"><a name=\"msg\"></a>\n";
		print "<b style=\"text-indent:18\">- �ԐM�t�H�[��</b>\n";
		print "�i���̋L���ɕԐM����ꍇ�͉��L�t�H�[�����瓊�e���ĉ������j<br>\n";
		print "<form action=\"$regist\" method=\"post\">\n";
		print "<input type=\"hidden\" name=\"mode\" value=\"form\">\n";
		print "<input type=\"hidden\" name=\"page\" value=\"$page\">\n";
		print "<input type=\"hidden\" name=\"action\" value=\"res_msg\">\n";
		print "<input type=\"hidden\" name=\"no\" value=\"$in{'no'}\">\n";
		print "<input type=\"hidden\" name=\"oya\" value=\"$in{'oya'}\">\n";
	# �V�K��
	} else {
		$wrap = 'soft';
		print "<hr width=\"95%\"><p><a name=\"msg\"></a><div align=\"center\">\n";
		print "<b><big>���b�Z�[�W���ǂ����E�E</big></b></a></div>\n";
		print "<P><form action=\"$regist\" method=\"post\">\n";
		print "<input type=\"hidden\" name=\"mode\" value=\"form\">\n";
		print "<input type=\"hidden\" name=\"page\" value=\"$page\">\n";
		print "<input type=\"hidden\" name=\"no\" value=\"new\">\n";
	}

	print "<blockquote><table border=\"0\" cellspacing=\"0\" cellpadding=\"1\">\n";
	print "<tr><td><b>���Ȃ܂�</b></td>";
	print "<td><input type=\"text\" name=\"name\" size=\"28\" value=\"$cname\"></td></tr>\n";
	print "<tr><td><b>�d���[��</b></td>";
	print "<td><input type=\"text\" name=\"email\" size=\"28\" value=\"$cmail\"> ";
	print "<select name=\"smail\">\n";

	@sm = ('�\��', '��\��');
	if ($csmail eq "") { $csmail=0; }
	foreach (0, 1) {
		if ($csmail == $_) {
			print "<option value=\"$_\" selected>$sm[$_]\n";
		} else {
			print "<option value=\"$_\">$sm[$_]\n";
		}
	}

 	print "</select></td></tr>\n";
	print "<tr><td><b>�^�C�g��</b></td>";
	print "<td><input type=\"text\" name=\"sub\" size=\"38\" value=\"$res_sub\"></td></tr>\n";
	print "<tr><td colspan=\"2\"><b>���b�Z�[�W</b>&nbsp;&nbsp;&nbsp;";

	@w1 = ('�蓮���s', '�������s', '�}�\���[�h');
	@w2 = ('soft', 'hard', 'pre');
	foreach (0 .. 2) {
		if ($wrap eq $w2[$_]) {
			print "<input type=\"radio\" name=\"wrap\" value=\"$w2[$_]\" checked>$w1[$_]\n";
		} else {
			print "<input type=\"radio\" name=\"wrap\" value=\"$w2[$_]\">$w1[$_]\n";
		}
	}

	# �v���r���[�̃`�F�b�N
	if ($cpv eq "on") { $checked = "checked"; }

	print "<br><textarea name=\"message\" rows=\"10\" cols=\"62\">$res_msg</textarea>";
	print "</td></tr><tr><td><b>�Q�Ɛ�</b></td>";
	print "<td><input type=\"text\" name=\"url\" size=\"58\" value=\"$curl\"></td></tr>\n";

	if ($_[0] eq "edt") {
		print "<tr><td></td><td><input type=\"submit\" value=\" �L�����C������ \"></td>\n";
		print "</tr></table></form></blockquote>\n";
	} else {
		print <<"EOM";
<tr>
  <td><b>�Ï؃L�[</b></td>
  <td><input type="password" name="pwd" size="8" value="$cpwd" maxlength=8>
	(�p������8�����ȓ�)</td>
</tr>
<tr>
  <td></td>
  <td><input type="submit" value=" �L���𓊍e���� ">
	 &nbsp; <input type="checkbox" name="pview" value="on" $checked>�v���r���[</td>
</tr>
</table>
</form>
</blockquote>
<hr width="95%">
<div align="center">
<form action="$regist" method="post">
<input type="hidden" name="page" value="$page">
<font color="$sub_color">
- �ȉ��̃t�H�[�����玩���̓��e�L�����C���E�폜���邱�Ƃ��ł��܂� -</font><br>
���� <select name="mode">
<option value="usr_edt">�C��
<option value="usr_del">�폜
</select>
�L��No <input type="text" name="no" size="4" style="ime-mode:inactive">
�Ï؃L�[ <input type="password" name="pwd" size="6">
<input type="submit" value="���M"></form>
<hr width="95%"></div>
EOM
	}
}

#---------------------------------------
#  �N�b�L�[�擾
#---------------------------------------
sub get_cookie {
	local($key, $val, *cook);

	# �N�b�L�[���擾
	$cook = $ENV{'HTTP_COOKIE'};

	# �Y��ID�����o��
	foreach ( split(/;/, $cook) ) {
		($key, $val) = split(/=/);
		$key =~ s/\s//g;
		$cook{$key} = $val;
	}

	# �f�[�^��URL�f�R�[�h���ĕ���
	foreach ( split(/<>/, $cook{'WFORUM'}) ) {
		s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("H2", $1)/eg;

		push(@cook,$_);
	}
	return (@cook);
}

#---------------------------------------
#  �N�b�L�[���s
#---------------------------------------
sub set_cookie {
	local(@cook) = @_;
	local($gmt, $cook, @t, @m, @w);

	@t = gmtime(time + 60*24*60*60);
	@m = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	@w = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	# ���ەW�������`
	$gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$w[$t[6]], $t[3], $m[$t[4]], $t[5]+1900, $t[2], $t[1], $t[0]);

	# �ۑ��f�[�^��URL�G���R�[�h
	foreach (@cook) {
		s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
		$cook .= "$_<>";
	}

	# �i�[
	print "Set-Cookie: WFORUM=$cook; expires=$gmt\n";
}

#-------------------------------------------------
#  �֎~���[�h�`�F�b�N
#-------------------------------------------------
sub no_wd {
	local($flg);
	foreach ( split(/,/, $no_wd) ) {
		if (index("$in{'name'} $in{'sub'} $in{'message'}",$_) >= 0) {
			$flg = 1; last;
		}
	}
	if ($flg) { &error("�֎~���[�h���܂܂�Ă��܂�"); }
}

#-------------------------------------------------
#  ���{��`�F�b�N
#-------------------------------------------------
sub jp_wd {
	local($sub, $com, $mat1, $mat2, $code1, $code2);
	$sub = $in{'sub'};
	$com = $in{'message'};
	if ($sub) {
		($mat1, $code1) = &jcode'getcode(*sub);
	}
	($mat2, $code2) = &jcode'getcode(*com);
	if ($code1 ne 'sjis' && $code2 ne 'sjis') {
		&error("�薼���̓R�����g�ɓ��{�ꂪ�܂܂�Ă��܂���");
	}
}

#-------------------------------------------------
#  URL���`�F�b�N
#-------------------------------------------------
sub urlnum {
	local($com) = $in{'message'};
	local($num) = ($com =~ s|(https?://)|$1|ig);
	if ($num > $urlnum) {
		&error("�R�����g����URL�A�h���X�͍ő�$urlnum�܂łł�");
	}
}


1;

