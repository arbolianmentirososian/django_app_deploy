#!/usr/bin/env bash

function display_usage() {
    echo "usage: $0 {PREPROD|SIT|SIT2|UAT}"
}

function perform_preprod_tests() {
    ### regression tests preprod ###
    echo "regression tests preprod"
}

function perform_sit_tests() {
    ### regression tests sit ###
    echo "regression tests sit"
}

function perform_support_tests() {
    ### regression tests support ###
    echo "regression tests support"
}

function perform_uat_tests() {
    ### regression tests uat ###
    echo "regression tests uat"
}


if [[ "$#" -ne 1 ]]; then
    echo "invalid number of parameters provided"
    display_usage
    exit 1
else 
    env=$1
    case $env in
        "PREPROD")
            perform_preprod_tests
            ;;
        "SIT")
            perform_sit_tests
            ;;
        "SIT2")
            perform_support_tests
            ;;
        "UAT")
            perform_uat_tests
            ;;
        *)
            echo "invalid environment provided"
            display_usage
            exit 1
            ;;
    esac
fi
