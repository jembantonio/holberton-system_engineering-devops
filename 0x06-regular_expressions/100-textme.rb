#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(?<from>[a-zA-Z0-9+-]+).*to:(?<to>[a-zA-Z0-9+-]+).*flags:(?<flags>[a-zA-Z0-9+-:]+)/).join(",")
