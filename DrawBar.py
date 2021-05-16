import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
# print(mpl.__version__)
from matplotlib.backends.backend_pdf import PdfPages
import argparse

def add_args():
    """
    return a parser added with args required by fit
    """
    parser = argparse.ArgumentParser(description='bar args')

    # 内容相关
    parser.add_argument('--data', type=str, default='', help='a string of data')

    parser.add_argument('--legend_list', type=str, default='', \
                        help='a string of list of legend')
    
    parser.add_argument('--y_label', type=str, default='', \
                        help='label of y-axis')

    # 结果相关
    parser.add_argument('--picture_name', type=str, default='figure1.pdf', \
                        help='name of file storing picture (include extension)')


    # 绘图相关
    parser.add_argument('--ymin', type=float, default=-99999, help='Y-axis display minimal')

    parser.add_argument('--ymax', type=float, default=99999, help='Y-axis display maximal')

    parser.add_argument('--font', type=str, default='Helvetica', help='font')

    parser.add_argument('--legend_position', type=int, default=1, \
                        help='position of lengend')
    
    parser.add_argument('--legend_column', type=int, default=1, \
                        help='column num in lengend')

    parser.add_argument('--linewidth', type=float, default=2, help='line width of hatch')

    parser.add_argument('--barwidth', type=float, default=0.618, help='width of bar')
    


    args = parser.parse_args()
    return args

def str2floatlist():
    '''
    todo: transform a string to a list of floats
    '''

def str2strlist():
    '''
    todo: transform a string to a list of strings
    '''

def y_limit(data_list, args):
    Y_MIN = 0
    Y_MAX = 0
    data_min = min(data_list)
    data_max = max(data_list)
    if data_max == 0 and data_min == 0:
        Y_MIN = -1
        Y_MAX = 1 
    elif data_min > 0:
        if args.ymin == -99999:
            Y_MIN = 0
        else:
            Y_MIN = args.ymin
        if args.ymax == 99999:
            Y_MAX = 1.2*data_max
        else:
            Y_MAX = args.ymax
    elif data_max < 0:
        if args.ymin == -99999:
            Y_MIN = 1.2*data_max
        else:
            Y_MIN = args.ymin
        if args.ymax == 99999:
            Y_MAX = 0
        else:
            Y_MAX = args.ymax
    else:
        if args.ymin == -99999:
            Y_MIN = 1.2*data_max
        else:
            Y_MIN = args.ymin
        if args.ymax == 99999:
            Y_MAX = 1.2*data_max
        else:
            Y_MAX = args.ymax
    return (Y_MIN, Y_MAX)                        


def main():
    # get all the program arguments.
    args = add_args()
    # data_list = str2floatlist(args.data)
    data_list = [712.6650, 220.5163, 232.7826, 524.5636]
    # legend_list = str2strlist(args.legend_list)
    legend_list = ['p=0.99,l=1,g=1','p=0.9,l=1,g=1','p=0.99,l=5,g=1','p=0.99,l=1,g=5']
    Y_limit = y_limit(data_list, args)
    lo = args.legend_position
    nco = args.legend_column
    x = 0.2
    fig = plt.figure(figsize=(5.2*(1/(1-x)),5.2), dpi = 100)

    color = [(0.3098, 0.5059, 0.74120), (0.6078, 0.7333, 0.3490), \
            (0.7490, 0.3137, 0.3020), (0.5000, 0.5000, 0.5000), \
            (0.9300, 0.6900, 0.1300), (0.3000, 0.7500, 0.9300),\
            (0.5000, 0.3900, 0.6400), (0.1500, 0.1500, 0.1500), \
            (0.1800, 0.6400, 0.5400)] 
    patterns = ['/', '\\', 'xx', 'x', '\\\\', '//', '+', '..', '++']

    mpl.rcParams["font.family"] = args.font
    mpl.rcParams['hatch.linewidth'] = args.linewidth

    FontSize1 = 18 # 小的字体
    FontSize2 = 26 # 大的字体
    X = 1
    XX = 1
    w = args.barwidth*XX
    X_limit = (1-w, len(data_list)+w/2+1-w)

    for i in range(len(data_list)):
        plt.bar(X+i*XX, data_list[i], width = args.barwidth, \
                facecolor = 'white',edgecolor = color[i], hatch=patterns[i], \
                linewidth = args.linewidth)

    plt.rc('legend', fontsize=FontSize1)
    plt.legend(legend_list, loc=lo, fancybox = False, edgecolor='black', \
                borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3, \
                ncol = nco)

    list1 = []
    list2 = []
    for i in range(len(data_list)):
        list1.append(X+i*XX)
        list2.append(' ')
    plt.xticks(list1, list2, fontsize=FontSize1)
    plt.yticks(fontsize=FontSize1)
    plt.xlabel(" ", fontsize=FontSize2)
    plt.ylabel(args.y_label, fontsize=FontSize2)

    plt.ylim(Y_limit)
    plt.xlim(X_limit)
    
    plt.subplots_adjust(left=x)

    plt.savefig("5.png")
    plt.show()

if __name__ == "__main__":
    main()