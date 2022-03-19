import csv,io,sys,requests
import pandas as pd

class Iana:
    def getIanaTCPdf(self, url='http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv'):
        """ Downloads the current iana.org port assignment csv and returns a df of tcp ports only)

            Example to search resultant DataFrame and return concatenation of any column by position: 

                ianadf = getIanaTCP()
                print('|'.join([*{*ianadf.loc[ianadf['Port Number'] == '80'].T.values.tolist()[3]}]))
                
                    position 0 to code
                    position 1 to port number
                    position 2 to protocol
                    position 3 to Long description

        """
        print("Downloading and processing: '%s'" % url, file=sys.stderr)
        return pd.DataFrame([x for x in (csv.DictReader(io.StringIO(requests.get(url).text))) if x['Transport Protocol'] == 'tcp'])




# ssh-agent bash -c 'ssh-add /somewhere/yourkey; git clone git@github.com:user/project.git'


echo "# get_iana_info" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa; git remote add origin https://github.com/guistela/get_iana_info.git'
ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa; git push -u origin main'