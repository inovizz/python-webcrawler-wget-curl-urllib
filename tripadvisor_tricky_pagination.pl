use Data::Dumper;
my @global_linksee;
sub paginationUrls{
    #print "hi\n";
	my (@url) = @_; 
    foreach(@url){
        #print $_."\n";
    	my $pageSource = `curl --silent '$_' -H 'User-Agent: Mozilla/5.0 (Macintosh; In grep OS X 10.9; rv:24.0) Gecko/20100101 Firefox/24.0' 2>/dev/null`;
        my @linksee;
        #push(@linksee,"$_");
    	if ($pageSource =~ m/<span\sclass\="pageNum\scurrent[^>]*>[^>]*>\s*<a href\=\"[^\"]*\"/){
    	   my @nextLinks = $pageSource =~ m{<span\sclass\="pageNum\scurrent[^>]*>[^>]*>\s*<a href\=\"([^\"]*)\"}g;
        
        foreach (@nextLinks) {
        	my $next1 = $_;
        	$next1 =~ s/^/http\:\/\/www\.tripadvisor\.in/si;
        	push(@linksee,"$next1");
            push(@global_linksee,"$next1");
        #print STDERR Dumper (\@linksee);
    	}
        print STDERR Dumper (\@global_linksee);
        if ($pageSource =~ m/<span class\=\"separator\">\&hellip\;/){
            foreach (@linksee) {
                print $_."\n";
                paginationUrls($_)
            }
        }
        else{
            print "Not found";
        }
    	#my $last_url = pop @linksee;
    	#for (my $i = 0; $i < 2; $i++) {
    	#	print "Here";
    	#paginationUrls ($last_url);
    	#print "$last_url";
    	print STDERR Dumper (\@global_linksee);
    }
    }
    } 
#}
paginationUrls("http://www.tripadvisor.in/Hotel_Review-g60898-d86238-Reviews-or10-Sheraton_Atlanta_Hotel-Atlanta_Georgia.html#REVIEWS");