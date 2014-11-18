#!/usr/bin/env python
"""
Contains methods used by the paasta client to list Yelp services
"""

from service_deployment_tools import marathon_tools


def get_services():
    """
    :return: a list of marathon services that are currently running
    """
    # TODO: Return all Yelp services, not just marathon services
    return marathon_tools.get_marathon_services_for_cluster()


def paasta_list():
    """
    Print a list of Yelp services currently running
    """
    for service in get_services():
        print service