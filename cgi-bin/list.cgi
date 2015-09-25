#!/usr/bin/perl

use CGI;
use DBI;

my $cgi = CGI->new();
my $dbh = DBI->connect("DBI:mysql:host=localhost;port=3306", "test", "test");

print $cgi->header();

my $sth = $dbh->prepare("SELECT fname, lname, address1, address2, city, state FROM cgi_example.submission ORDER BY id DESC");

my $result = $sth->execute();

@template = ();

open (READ, "<list.tpl"), @template = <READ>, close(READ);

$num_lines = @template;
$current_line = "";

$i = 0;

while ($i < $num_lines && $current_line !~ /%%TBODY-START%%/) {
	print $current_line;
	$current_line = $template[$i];
	$i += 1;
}

while ($result = $sth->fetchrow_hashref()) {
	
	print "<tr>\n";
	print "<td>" . $result->{fname} . "</td>\n";
	print "<td>" . $result->{lname} . "</td>\n";
	print "<td>" . $result->{address1} . "</td>\n";
	print "<td>" . $result->{address2} . "</td>\n";
	print "<td>" . $result->{city} . "</td>\n";
	print "<td>" . $result->{state} . "</td>\n";
	print "</tr>\n";

}

$i += 1;

while ($i < $num_lines) {
	print $template[$i];
	$i += 1;
}


