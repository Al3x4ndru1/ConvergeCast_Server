#!/bin/bash
function get_network(){
    #interface=
    x= ifconfig wlp3s0 | head -2 | tail -1 ; return $x | cut -d ' ' -f2
    return "$x"
}
a=$get_network
echo "$a"