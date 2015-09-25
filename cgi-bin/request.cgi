#!/usr/bin/perl

use DBI;
use CGI;
use Data::Dumper;


my $cgi = CGI->new();
my $dbh = DBI->connect("DBI:mysql:host=localhost;port=3306", "test", "test");


if ($dbh->err) {
	print STDERR $dbh->errstr and die "Internal Server Error";
}


my %vars = $cgi->Vars;

my $q = "INSERT INTO cgi_example.submission (fname, lname, address1, address2, city, state) VALUES (?, ?, ?, ?, ?, ?)";

my $sth = $dbh->prepare($q);


$sth->bind_param(1, $vars{fname});
$sth->bind_param(2, $vars{lname});
$sth->bind_param(3, $vars{address1});
$sth->bind_param(4, $vars{address2});
$sth->bind_param(5, $vars{city});
$sth->bind_param(6, $vars{state});

$sth->execute();

if ($sth->err) {
	print STDERR $sth->errstr;
}

print $cgi->redirect(
	-uri => 'http://localhost/cgi-bin/list.cgi',
	-status => '302 Found'
);

