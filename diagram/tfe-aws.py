#!/usr/bin/env python3

from diagrams import Diagram
from diagrams.aws.compute import EC2Instance
from diagrams.aws.compute import EC2ElasticIpAddress
from diagrams.aws.network import VPC


with Diagram("TFE AWS", show=False, direction="TB"):
    EC2ElasticIpAddress("TFE IP") >> VPC("tfe vpc") >> EC2Instance("Amazon Linux")
