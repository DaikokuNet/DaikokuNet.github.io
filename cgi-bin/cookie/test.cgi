#!/usr/local/bin/perl
# Content-type�w�b�_���o��
print "Content-type: text/html\n";

# Set-Cookie�w�b�_���o��
print "Set-Cookie: ";
print "TEST2=2; ";
print "expires=Friday, 31-Dec-2002 00:00:00 GMT; ";
print "path=/~masa-nak/cgi-bin/cookie; "; 
print "domain=www2s.biglobe.ne.jp\n";

# �w�b�_�̏I�����o��
print "\n";

print <<EOM;
<HTML>
<HEAD>
<TITLE>TEST</TITLE>
</HEAD>
<BODY>
This is a test.<BR>
$ENV{'HTTP_COOKIE'}
</BODY>
</HTML>
EOM
