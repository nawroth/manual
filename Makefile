# Makefile for the Neo4j Manual.
#
# Note: requires mvn to unpack some stuff first.

# Project Configuration
project_name               = neo4j-manual
language                   = en

# Minimal setup
target                     = target
config_dir                 = $(CURDIR)/src/main/conf
build_dir                  = $(CURDIR)/$(target)
tools_dir                  = $(build_dir)/tools
make_dir                   = $(tools_dir)/make

include $(make_dir)/context-manual.make


