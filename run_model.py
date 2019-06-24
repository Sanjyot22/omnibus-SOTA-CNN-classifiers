import argparse
from trainKerasModel import kerasModelTraining

"""
All the recognition models available:

keras_models= ['xception', 'vgg16', 'vgg19', 'resnet50', 'inceptionv3', 
                'inceptionresnetv2', 'nasnet_small','nasnet_large',
                'densenet121', 'densenet169', 'densenet201', 'mobilenet']
keras_contrib_models = ['wideresnet','ror']
other = ['resnet101','resnet152']
all_other = ['resnet18','resnet34','squeezenet1_0','squeezenet1_1','vgg11','vgg13','resnext101_64x4d','resnext101_32x4d','inceptionv4']
"""


def print_arguments():
    print('task : ',args.task)
    print('data_dir_train : ',args.data_dir_train)
    print('data_dir_valid : ',args.data_dir_valid)
    print('data_dir_test : ',args.data_dir_test)
    print('model_name : ',args.model_name)
    print('epochs : ',args.epochs)
    print('batch_size :',args.batch_size)
    print('training_type :',args.training_type)
    print('save_loc : ',args.save_loc)
    print('weights : ',args.weights)
    print('results_loc : \n',args.results_loc)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Training a Image Classification model')

    required = parser.add_argument_group('required arguments')
    required.add_argument('-t', '--task',help = 'Train or Test',required = True)
    required.add_argument('-dtrain', '--data_dir_train', help='Path to Training Data')
    required.add_argument('-dvalid', '--data_dir_valid',help='Path to Validation Data')

    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('-dtest', '--data_dir_test', default="./data/testing_data", help='Path to Testing Data')
    optional.add_argument('-m', '--model_name', default="resnet50",help = 'Pretrianed model name')
    optional.add_argument('-e', '--epochs', default=100, type=int, help = 'Number of epochs')
    optional.add_argument('-b', '--batch_size', default=32, type=int , help = 'Batch-size')
    optional.add_argument('-clear', '--clear', default=False, help = 'Clear earlier model logs')


    #We will be using 3 Training Types - 1 : Fine tune all network , 2: Freeze some starting layers
    optional.add_argument('-tt', '--training_type',default = "train_all",help = 'Fine tune all network: fine_tune , Freeze the starting layers : freeze')
    optional.add_argument('-s', '--save_loc', default="models/" ,help = 'Save location for the trained models')
    optional.add_argument('-w', '--weights',default = 'imagenet', help='weights imagenet or custom')
    optional.add_argument('-r', '--results_loc',default = 'results/', help='Save location for the test results')



    """
    #additional options for v2
    optional.add_argument('-cs', '--crop-size', type=int, default=512, help='Crop size')
    optional.add_argument('-p', '--pooling', type=str, default='avg', help='Type of pooling to use: avg|max|none')
    optional.add_argument('-do', '--dropout', type=float, default=0.3, help='Dropout rate for FC layers')
    optional.add_argument("-p", '--use_parallel', default=False, action='store_true')
    optional.add_argument("-a", '--aug', default=False, action='store_true',help = 'Apply Basic Augumentation or not' )
    optional.add_argument("-act", '--activation', default= 'relu' , help = 'Activation Function to be used')
    optional.add_argument('-o', '--optimizer',default = "sgd", help = 'The optimizer to be used')
    optional.add_argument("-g", '--no_of_gpus', default=1,help = 'No of GPUs to be used for training)
    """


    args = parser.parse_args()
    print_arguments()


    if args.task.lower() == 'train':
        training_object = kerasModelTraining(args.data_dir_train,args.data_dir_valid,args.batch_size,
                                             args.epochs,args.model_name,args.training_type,args.save_loc,
                                             args.weights,args.clear)
        output_string = training_object.train()
    # elif args.task.lower() == 'test':
        # output_string = test.test_model(args.data_dir_train,args.data_dir_test,args.batch_size,args.model_name,args.save_loc,args.results_loc)
    else:
        output_string = "Incorrect Task"

    print(output_string)