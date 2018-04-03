import yaml
try:
    from yaml import  CLoader as Loader,CDumper as Dumper
except ImportError:
    from yaml import  Loader,Dumper




def readyamlfile():
    return yaml.load(open('111.yml','r'))


a = readyamlfile()
print(a,type(a))