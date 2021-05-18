import os
import argparse
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



def add_args():
    """
    return a parser added with args required by fit
    """
    parser = argparse.ArgumentParser(description='bar args')

    # 内容相关
    parser.add_argument('--data', nargs='+', type=float,\
                        help='a string of data')

    parser.add_argument('--legend_list', nargs='+', type=str, \
                        help='a string of list of legend')
    
    parser.add_argument('--y_label', type=str, default='', \
                        help='label of y-axis')
    
    parser.add_argument('--x_label', type=str, default='', \
                        help='label of x-axis')    

    # 结果相关
    parser.add_argument('--picture_name', type=str, default='figure1.pdf', \
                        help='name of file storing picture (include extension)')


    # 绘图相关
    parser.add_argument('--ymin', type=float, default=-99999, \
                        help='Y-axis display minimal')

    parser.add_argument('--ymax', type=float, default=99999, \
                        help='Y-axis display maximal')

    parser.add_argument('--font', type=str, default='Helvetica', \
                        help='font')

    parser.add_argument('--legend_position', type=int, default=1, \
                        help='position of lengend')
    
    parser.add_argument('--legend_column', type=int, default=1, \
                        help='column num in lengend')
    
    parser.add_argument('--legend_fontsize', type=int, default=18, \
                        help='font size of legend')    

    parser.add_argument('--xticks_fontsize', type=int, default=18, \
                        help='font size of xticks')

    parser.add_argument('--yticks_fontsize', type=int, default=18, \
                        help='font size of yticks')

    parser.add_argument('--xlabel_fontsize', type=int, default=26, \
                        help='font size of xticks')

    parser.add_argument('--ylabel_fontsize', type=int, default=26, \
                        help='font size of yticks')
    
    parser.add_argument('--linewidth', type=float, default=2, \
                        help='line width of bar and hatch')

    parser.add_argument('--barwidth', type=float, default=0.618, \
                        help='width of bar (from 0 to 1)')
    


    args = parser.parse_args()
    return args

def calculate_y_limit(data_list, args):
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
    data_list = args.data
    legend_list = args.legend_list
    if len(data_list) != len(legend_list):
        print("ERROR: length of data does not equal to length of legend!")
        return 0

    Y_limit = calculate_y_limit(data_list, args)

    x = 0.2
    '''
    todo: 图窗相关
    '''
    fig = plt.figure(figsize=(5.2*(1/(1-x)),5.2), dpi = 100)

    color = [(0.3098, 0.5059, 0.74120), (0.6078, 0.7333, 0.3490), \
            (0.7490, 0.3137, 0.3020), (0.5000, 0.5000, 0.5000), \
            (0.9300, 0.6900, 0.1300), (0.3000, 0.7500, 0.9300),\
            (0.5000, 0.3900, 0.6400), (0.1500, 0.1500, 0.1500), \
            (0.1800, 0.6400, 0.5400)] 
    patterns = ['/', '\\', 'xx', 'x', '\\\\', '//', '+', '..', '++']

    # 检查字体可用性
    ttf_list = os.listdir(mpl.matplotlib_fname()[:-12]+'fonts/ttf/')
    if args.font + '.ttf' in ttf_list:
        mpl.rcParams["font.family"] = args.font
    else:
        print('ERROR: the font ' + args.font + ' is not in font-lib of matplotlib! ' + \
                'You can add the .ttf file of the font you need into ' + \
                mpl.matplotlib_fname()[:-12]+'fonts/ttf/')
        return 0

    mpl.rcParams['hatch.linewidth'] = args.linewidth

    X_limit = (1-args.barwidth, len(data_list)+args.barwidth/2+1-args.barwidth)

    for i in range(len(data_list)):
        plt.bar(i+1, data_list[i], width = args.barwidth, \
                facecolor = 'white',edgecolor = color[i], hatch=patterns[i], \
                linewidth = args.linewidth)

    plt.rc('legend', fontsize=args.legend_fontsize)
    plt.legend(legend_list, loc=args.legend_position, fancybox = False, edgecolor='black', \
                borderpad = 0.2, labelspacing = 0.2, handletextpad = 0.3, \
                ncol = args.legend_column)

    list1 = []
    list2 = []
    for i in range(len(data_list)):
        list1.append(i+1)
        list2.append(' ')
    plt.xticks(list1, list2, fontsize=args.xticks_fontsize)
    plt.yticks(fontsize=args.yticks_fontsize)
    plt.xlabel(args.x_label, fontsize=args.xlabel_fontsize)
    plt.ylabel(args.y_label, fontsize=args.ylabel_fontsize)

    plt.ylim(Y_limit)
    plt.xlim(X_limit)
    
    plt.subplots_adjust(left=x)

    # 按照文件名选择保存格式
    if args.picture_name[-4:] == '.png' or args.picture_name[-4:] == '.jpg':
        plt.savefig(args.picture_name)
    elif args.picture_name[-4:] == '.pdf':
        pdf = PdfPages(args.picture_name)
        pdf.savefig()
        pdf.close()
    else:
        print('Warning: you choose a filetype not supported by this tool. ' + \
            'The picture will be stored as filetype .png.')
        dot_place = len(args.picture_name)
        for i in range(len(args.picture_name)):
            if args.picture_name[len(args.picture_name)-1-i] == '.':
                dot_place = len(args.picture_name)-1-i
                break
        if dot_place == 0:
            if len(args.picture_name) != 1:
                plt.savefig(args.picture_name[1:]+'.png')
            else:
                print('Warning: the filename input has only a point. ' + \
                    'The picture will be stored as 1.png.')
                plt.savefig('1.png')
        else:
            plt.savefig(args.picture_name[:dot_place]+'.png')

if __name__ == "__main__":
    main()