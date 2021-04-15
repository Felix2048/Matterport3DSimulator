cd data/v1/scans/
# for i in `ls -1 | grep $`; do cd $i && unzip "*.zip" && mv ./$i/* ./ && rm -r $i && cd ..; done
# for i in `ls -1 | grep $`; do cd $i && rm ./*.zip && cd ..; done
for i in `ls -1 | grep $`; do cd $i && unzip "*.zip" && mv ./$i/* ./ && rm -r $i && rm ./*.zip && cd ..; done
