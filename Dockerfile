FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y build-essential libreadline-dev ruby-dev python3.9-dev python3-pip

RUN gem install nokogiri json bundler sass mjai

RUN python3.9 -m pip install mjx==0.0.6
