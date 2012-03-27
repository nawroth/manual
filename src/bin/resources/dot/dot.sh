#!/bin/bash


fontpath=$1
targetimage=$2
generategraphviz=$3
colorset=$4

if [[ "$generategraphviz" == "0" ]]
then
  echo ""
  exit 0
fi

nodefontsize=10
edgefontsize=$nodefontsize
nodefontcolor="#1c2021" # darker grey
edgefontcolor=$nodefontcolor
edgecolor="#2e3436" # dark grey
boxcolor=$edgecolor
edgehighlight="#a40000" # dark red
nodefillcolor="#ffffff"
nodehighlight="#fcee7d" # lighter yellow
nodehighlight2="#fcc574" # lighter orange
nodeshape=box

# "#a8e270" # lighter green
# "#95bbe3" # lighter blue

if [[ "$colorset" == "meta" ]]
then
  nodefillcolor="#fadcad" # lighter brown
  nodehighlight="#a8e270" # lighter green
  nodehighlight2="#95bbe3" # lighter blue
elif [[ "$colorset" == "neoviz" ]]
then
  nodeshape=Mrecord
  nodefontsize=8
  edgefontsize=$nodefontsize
fi

graphsettings="graph [size=\"7.0,9.0\" fontpath=\"${fontpath}\"]"

nodestyle=filled,rounded
#nodeheight=0.37
nodesep=0.4
textnode=shape=plaintext,style=diagonals,height=0.2,margin=0.0,0.0

arrowhead=vee
arrowsize=0.75

indata=$(cat);
indata=${indata//NODEHIGHLIGHT/$nodehighlight}
indata=${indata//NODE2HIGHLIGHT/$nodehighlight2}
indata=${indata//EDGEHIGHLIGHT/$edgehighlight}
indata=${indata//BOXCOLOR/$boxcolor}
indata=${indata//TEXTNODE/$textnode}

svgfile=$targetimage
pngfile="${svgfile}.png"

graphfont="Liberation Sans"
nodefont=$graphfont
edgefont=$graphfont


prepend="digraph g{ $graphsettings\
  node [shape=\"$nodeshape\" penwidth=1.5 fillcolor=\"$nodefillcolor\" color=\"$boxcolor\" \
   fontcolor=\"$nodefontcolor\" style=\"$nodestyle\" fontsize=$nodefontsize \
   fontname=\"$nodefont\"]
  edge [color=\"$boxcolor\" penwidth=2 arrowhead=\"$arrowhead\" arrowtail=\"$arrowhead\" \
   arrowsize=$arrowsize fontcolor=\"$edgefontcolor\"\
   fontsize=$edgefontsize fontname=\"$edgefont\"] \
  nodesep=$nodesep \
  fontname=\"$graphfont\" "

echo "${prepend} ${indata} }" | dot -Tpng -o"$pngfile"
echo "${prepend} ${indata} }" | dot -Tsvg | sed -e 's/ font-family="Liberation Sans"//g' -e 's/?>/?><?xml-stylesheet type="text\/css" href="svg.css" ?>/' > "$svgfile"
#echo "${prepend} ${indata} }" > "${svgfile}.dot"

echo ""

