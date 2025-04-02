import json
import numpy as np
from matplotlib import pyplot as plt

experiments_names = ['minmal_steiner_vary_with_keywords_num',
                     'compare_head_tail_keywords_in_mashup',
                     'minmal_steiner_vary_with_keywords_num_in_mashup',
                     'compare_vary_with_keywords_num_in_mashup',
                     'compare_vary_with_keywords_num']

def load_result(filename):
    with open('../data/outputs/%s.json' % (filename), 'r') as f:
        dict = json.load(f)

        return np.array(dict['num_nodes']), np.array(dict['costs'])



def draw_nodes_found_by_minimal_steiner_with_head_tail():
    num_nodes, costs = load_result(experiments_names[1])

    average_num_nodes = np.average(num_nodes[0], axis =1)

    keyword_num_options = [2, 3, 4, 5, 6]
    plt.xlabel('l: number of keywords')
    plt.xticks(keyword_num_options)
    plt.ylim(0, 4)
    plt.ylabel('number of nodes')
    plt.plot(keyword_num_options, average_num_nodes, marker='*')

    with open('../data/outputs_res/nodes_found_by_minimal_with_head_tail.json', 'w') as f:
        json.dump(average_num_nodes.tolist(), f)

    plt.savefig('../data/outputs/nodes_found_by_minimal_with_head_tail.png')
    plt.show()

def draw_nodes_found_by_minimal_steiner_without_mashup():
    num_nodes, costs = load_result(experiments_names[4])

    average_num_nodes = np.average(num_nodes, axis =2)
    average_costs = np.average(costs, axis = 1)

    keyword_num_options = [2, 3, 4, 5, 6]
    plt.xlabel('l: number of keywords')
    plt.xticks(keyword_num_options)
    plt.ylabel('number of nodes')
    plt.plot(keyword_num_options, average_num_nodes[0], marker='*')
    with open('../data/outputs_res/nodes_found_by_minimal_without_mashup.json', 'w') as f:
        json.dump(average_num_nodes.tolist(), f)

    plt.savefig('../data/outputs/nodes_found_by_minimal_without_mashup.png')
    plt.show()

def draw_nodes_found_by_minimal_steiner_with_mashup():
    num_nodes, costs = load_result(experiments_names[3])

    average_num_nodes = np.average(num_nodes, axis =2)
    average_costs = np.average(costs, axis = 1)

    keyword_num_options = [2, 3, 4, 5, 6]
    plt.xlabel('l: number of keywords')
    plt.xticks(keyword_num_options)
    plt.ylabel('number of nodes')
    plt.plot(keyword_num_options, average_num_nodes[0], marker='*')
    with open('../data/outputs_res/nodes_found_by_minimal_with_mashup.json', 'w') as f:
        json.dump(average_num_nodes.tolist(), f)

    plt.savefig('../data/outputs/nodes_found_by_minimal_with_mashup.png')
    plt.show()

def draw_costs_by_minimal_steiner_with_head_tail():
    num_nodes, costs = load_result(experiments_names[1])

    average_costs = np.average(costs[0], axis =1)

    keyword_num_options = [2, 3, 4, 5, 6]
    plt.xlabel('l: number of keywords')
    plt.xticks(keyword_num_options)
    plt.ylim(0, 0.1)
    plt.ylabel('computation time (s)')
    plt.plot(keyword_num_options, average_costs, marker='*')

    plt.savefig('../data/outputs/costs_by_minimal_with_head_tail.png')
    plt.show()

    with open('../data/outputs_res/costs_by_minimal_with_head_tail.json', 'w') as f:
        json.dump(average_costs.tolist(), f)


def draw_nodes_with_different_methods():
    num_nodes, costs = load_result(experiments_names[3])

    average_num_nodes = np.average(num_nodes, axis=2)

    print(average_num_nodes)

    keyword_num_options = np.array([2, 3, 4, 5, 6])

    total_width, n = 0.8, 3
    width = total_width / n
    x = keyword_num_options - (total_width - width)/2.0

    plt.xlabel('l: number of keywords')
    plt.ylabel('number of nodes')
    plt.bar(x, average_num_nodes[0], width=width, label='K-CMR')
    plt.bar(x + width, average_num_nodes[2], width=width, label='Greedy')
    plt.bar(x + 2 * width, average_num_nodes[1], width=width, label='Random')

    plt.legend(loc='upper left')
    plt.savefig('../data/outputs/nodes_found_by_methods_with_head_tail.png')

    with open('../data/outputs_res/nodes_found_by_methods_with_head_tail.json', 'w') as f:
        json.dump(average_num_nodes.tolist(), f)

def draw_nodes_with_different_methods_without_mashup():
    num_nodes, costs = load_result(experiments_names[4])

    average_num_nodes = np.average(num_nodes, axis=2)

    print(average_num_nodes)

    keyword_num_options = np.array([2, 3, 4, 5, 6])

    total_width, n = 0.8, 3
    width = total_width / n
    x = keyword_num_options - (total_width - width)/2.0

    plt.xlabel('l: number of keywords')
    plt.ylabel('number of nodes')
    plt.bar(x, average_num_nodes[0], width=width, label='K-CMR')
    plt.bar(x + width, average_num_nodes[2], width=width, label='Greedy')
    plt.bar(x + 2 * width, average_num_nodes[1], width=width, label='Random')

    plt.legend(loc='upper left')
    plt.savefig('../data/outputs/nodes_found_by_methods_without_mashup.png')
    with open('../data/outputs_res/nodes_found_by_methods_without_mashup.json', 'w') as f:
        json.dump(average_num_nodes.tolist(), f)

def draw_success_rates_of_different_methods():
    num_nodes, costs = load_result(experiments_names[3])
    sample_count = 24
    success_rates = np.zeros((3, 5))

    keyword_num_options = np.array([2, 3, 4, 5, 6])

    for i in range(3):
        for (idx, num) in enumerate(keyword_num_options):
            success_rates[i, idx] = np.sum(num_nodes[i, idx, :] <= num * 3) * 100.0 / sample_count

    print(success_rates)
    total_width, n = 0.8, 3
    width = total_width / n
    x = keyword_num_options - (total_width - width)/2.0


    plt.xlabel('l: number of keywords')
    # plt.xlim(1, 8)
    plt.ylabel('success rate (%)')
    plt.ylim(0, 125)
    plt.yticks([20, 40, 60, 80, 100])
    plt.bar(x, success_rates[0], width=width, label='K-CMR')
    plt.bar(x + width, success_rates[2], width=width, label='Greedy')
    plt.bar(x + 2 * width, success_rates[1], width=width, label='Random')

    plt.legend(loc='upper right')
    plt.savefig('../data/outputs/success_rates_of_methods_with_head_tail_by3.png')
    plt.show()
    with open('../data/outputs_res/success_rates_of_methods_with_head_tail.json', 'w') as f:
        json.dump(success_rates.tolist(), f)

def draw_success_rates_of_different_methods_without_mashup():
    num_nodes, costs = load_result(experiments_names[4])
    sample_count = 100
    success_rates = np.zeros((3, 5))

    keyword_num_options = np.array([2, 3, 4, 5, 6])

    for i in range(3):
        for (idx, num) in enumerate(keyword_num_options):
            success_rates[i, idx] = np.sum(num_nodes[i, idx, :] <= num * 3) * 100.0 / sample_count

    print(success_rates)
    total_width, n = 0.8, 3
    width = total_width / n
    x = keyword_num_options - (total_width - width)/2.0


    plt.xlabel('l: number of keywords')
    # plt.xlim(1, 8)
    plt.ylabel('success rate (%)')
    plt.ylim(0, 125)
    plt.yticks([20, 40, 60, 80, 100])
    plt.bar(x, success_rates[0], width=width, label='K-CMR')
    plt.bar(x + width, success_rates[2], width=width, label='Greedy')
    plt.bar(x + 2 * width, success_rates[1], width=width, label='Random')

    plt.legend(loc='upper right')
    plt.savefig('../data/outputs/success_rates_of_methods_without_mashup.png')
    plt.show()
    with open('../data/outputs_res/success_rates_of_methods_without_mashup.json', 'w') as f:
        json.dump(success_rates.tolist(), f)

def draw_costs_with_different_methods():
    '''
    对比三种不同的方法，在给定mashup中的keywords的前提下，返回结果所花费的时间
    :param e_index: 1, 对比只给mashup中的第一个和最后一个keyword时查询的时间开销；
                    2，给出mashup所有的keyword的时间开销
    :return:
    '''
    num_nodes, costs = load_result(experiments_names[3])

    average_costs = np.average(costs, axis=2)
    log_average_costs = np.log(average_costs)

    keyword_num_options = np.array([2, 3, 4, 5, 6])

    plt.xlabel('l:number of keywords')
    plt.xticks(keyword_num_options)

    plt.ylabel(r'computation time ($log_2$)')
    plt.plot(keyword_num_options, log_average_costs[0], marker='*', label='K-CMR')
    plt.plot(keyword_num_options, log_average_costs[2], marker='*', label='Greedy')
    plt.plot(keyword_num_options, log_average_costs[1], marker='*', label='Random')
    plt.legend()
    # plt.show()
    plt.savefig('../data/outputs/log_costs_of_methods.png')
    with open('../data/outputs_res/log_costs_of_methods.json', 'w') as f:
        json.dump(log_average_costs .tolist(), f)

def draw_costs_with_different_methods_without_mashup():
    '''
    对比三种不同的方法，在给定mashup中的keywords的前提下，返回结果所花费的时间
    :param e_index: 1, 对比只给mashup中的第一个和最后一个keyword时查询的时间开销；
                    2，给出mashup所有的keyword的时间开销
    :return:
    '''
    num_nodes, costs = load_result(experiments_names[4])

    average_costs = np.average(costs, axis=2)
    log_average_costs = np.log(average_costs)

    keyword_num_options = np.array([2, 3, 4, 5, 6])

    plt.xlabel('l:number of keywords')
    plt.xticks(keyword_num_options)

    plt.ylabel(r'computation time ($log_2$)')
    plt.plot(keyword_num_options, log_average_costs[0], marker='*', label='K-CMR')
    plt.plot(keyword_num_options, log_average_costs[2], marker='*', label='Greedy')
    plt.plot(keyword_num_options, log_average_costs[1], marker='*', label='Random')
    plt.legend()
    # plt.show()
    plt.savefig('../data/outputs/log_costs_of_methods_without_mashup.png')
    with open('../data/outputs_res/log_costs_of_methods_without_mashup.json', 'w') as f:
        json.dump(log_average_costs .tolist(), f)





# draw_success_rates_of_different_methods()
# draw_success_rates_of_different_methods_without_mashup()

# draw_nodes_with_different_methods()
# draw_nodes_with_different_methods_without_mashup()

# draw_costs_with_different_methods()
draw_costs_with_different_methods_without_mashup()

# draw_nodes_found_by_minimal_steiner_with_mashup()
# draw_nodes_found_by_minimal_steiner_without_mashup()



# draw_nodes_found_by_minimal_steiner_with_head_tail()



