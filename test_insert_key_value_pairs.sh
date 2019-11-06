#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle insert_key_value_pairs.py
assert_no_stdout
run test_style pycodestyle test_binary_tree.py
assert_no_stdout
run test_style pycodestyle test_avl_tree.py
assert_no_stdout
run test_style pycodestyle binary_tree.py
assert_no_stdout

run test_bad_pair python3 insert_key_value_pairs.py --data_structure hash --dataset rand.txt --kv_pairs_number 10001
assert_exit_code 1
run test_bad_pair python3 insert_key_value_pairs.py --data_structure hash --dataset rand.txt --kv_pairs_number 0
assert_exit_code 1
run test_bad_input_file python3 insert_key_value_pairs.py --data_structure avl_tree --dataset bad.txt --kv_pairs_number 1000
assert_exit_code 1
run test_bad_data_structure python3 insert_key_value_pairs.py --data_structure bad --dataset aaa.txt --kv_pairs_number 1000
assert_exit_code 1

run test_hash_rand python3 insert_key_value_pairs.py --data_structure hash --dataset rand.txt --kv_pairs_number 10000
assert_exit_code 0
assert_stdout

run test_hash_sorted python3 insert_key_value_pairs.py --data_structure hash --dataset sorted.txt --kv_pairs_number 10000
assert_exit_code 0
assert_stdout

run test_binary_rand python3 insert_key_value_pairs.py --data_structure binary_tree --dataset rand.txt --kv_pairs_number 10000
assert_exit_code 0
assert_stdout

run test_binary_sorted python3 insert_key_value_pairs.py --data_structure binary_tree --dataset sorted.txt --kv_pairs_number 10000
assert_exit_code 0
assert_stdout

run test_avl_rand python3 insert_key_value_pairs.py --data_structure avl_tree --dataset rand.txt --kv_pairs_number 10000
assert_exit_code 0
assert_stdout

run test_avl_sorted python3 insert_key_value_pairs.py --data_structure avl_tree --dataset sorted.txt --kv_pairs_number 10000
assert_exit_code 0
assert_stdout
