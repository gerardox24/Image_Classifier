import os

def main():
    for folder in os.listdir('datasets'):
        n = 1
        for imgfile in os.listdir('datasets/'+folder):
            dst = 'datasets/'+folder+'/'+folder+'-{:03}.jpg'.format(n)
            src = 'datasets/'+folder+'/'+imgfile
            n += 1
            os.rename(src,dst)
            print(dst)

if __name__ == '__main__':
    main()