import sys
import os
import importlib
import binary_tree
sys.path.append('avl_tree')  # noqa: E402
sys.path.append('hash-tables-rymo1354')  # noqa: E402
hash_tables = importlib.import_module('hash-tables-rymo1354.hash_tables')  # noqa: E402
hash_functions = importlib.import_module('hash-tables-rymo1354.hash_functions')  # noqa: E402
avl = importlib.import_module('avl_tree.avl')  # noqa: E402
import argparse
import time


def parse_args():
    parser = argparse.ArgumentParser(
        description='The right way to pass parameters.',
        prog='insert_key_value_pairs.py')

    parser.add_argument('--data_structure',
                        type=str,
                        help='Specify the data structure used',
                        required=True)

    parser.add_argument('--dataset',
                        type=str,
                        help='File name of the dataset',
                        required=True)

    # require number of data
    parser.add_argument('--kv_pairs_number',
                        type=int,
                        help='Number of key/value pairs used',
                        required=True)

    return parser.parse_args()


def dataset_keys(dataset, number_of_keys):
    count = 1
    keys = []
    for l in open(args.dataset):
        if count <= number_of_keys:
            keys.append(l)
            count += 1
        else:
            break
    return keys


def hash(keys):
    hash_table = hash_tables.ChainedHash(100000, hash_functions.h_ascii)
    # insert
    insert_start = time.time()
    for key in keys:
        hash_table.add(key, key)
    insert_end = time.time()
    # search existing keys
    esearch_start = time.time()
    for key in keys:
        hash_table.search(key)
    esearch_end = time.time()
    # search non-existing keys
    nesearch_start = time.time()
    for key in keys:
        hash_table.search(key + '_not_in_table')
    nesearch_end = time.time()
    # total time
    insert = insert_end - insert_start
    esearch = esearch_end - esearch_start
    nesearch = nesearch_end - nesearch_start

    return insert, esearch, nesearch


def print_times(insert, esearch, nesearch):
    print('Insert time: ' + str(insert))
    print('Existing key search time: ' + str(esearch))
    print('Non-existing key search time: ' + str(nesearch))


def avl_tree(keys):
    avl_tree = avl.AVL()
    # insert
    insert_start = time.time()
    for key in keys:
        avl_tree.insert(key)
    insert_end = time.time()
    # search existing keys
    esearch_start = time.time()
    for key in keys:
        avl_tree.find(key)
    esearch_end = time.time()
    # search non-existing keys
    nesearch_start = time.time()
    for key in keys:
        avl_tree.find(key + '_not_in_tree')
    nesearch_end = time.time()
    # total time
    insert = insert_end - insert_start
    esearch = esearch_end - esearch_start
    nesearch = nesearch_end - nesearch_start

    return insert, esearch, nesearch


def binary_tree_fxn(keys):
    binarytree = binary_tree.BinaryTree()
    # insert
    insert_start = time.time()
    for key in keys:
        binarytree.insert(key)
    insert_end = time.time()
    # search existing keys
    esearch_start = time.time()
    for key in keys:
        binarytree.search(key)
    esearch_end = time.time()
    # search non-existing keys
    nesearch_start = time.time()
    for key in keys:
        binarytree.search(key + '_not_in_tree')
    nesearch_end = time.time()
    # total time
    insert = insert_end - insert_start
    esearch = esearch_end - esearch_start
    nesearch = nesearch_end - nesearch_start

    return insert, esearch, nesearch


if __name__ == '__main__':
    args = parse_args()

    if args.kv_pairs_number > 10000 or args.kv_pairs_number < 1:
        print('Too many key/value pairs')
        sys.exit(1)
    if not os.path.exists(args.dataset):
        print('Dataset path does not exist')
        sys.exit(1)

    keys = dataset_keys(args.dataset, args.kv_pairs_number)

    if args.data_structure == 'hash':
        insert, esearch, nesearch = hash(keys)
        print_times(insert, esearch, nesearch)
    elif args.data_structure == 'avl_tree':
        insert, esearch, nesearch = avl_tree(keys)
        print_times(insert, esearch, nesearch)
    elif args.data_structure == 'binary_tree':
        insert, esearch, nesearch = binary_tree_fxn(keys)
        print_times(insert, esearch, nesearch)
    else:
        print('Not a valid data_structure')
        sys.exit(1)
