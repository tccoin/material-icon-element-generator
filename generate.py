# coding=utf-8
import json
import os
from urllib import request
import xmltodict
import re
import ssl
import certifi

currentPath = os.path.split(os.path.realpath(__file__))[0] + os.sep + '{}'


def readJson(inputFile):
    with open(currentPath.format(inputFile), 'r') as f:
        return json.load(f)


def getSVG(icon):
    temp = currentPath.format(os.path.join(
        'tmp', config['style']+'_'+icon+'.svg'))
    if os.path.exists(temp):
        with open(temp) as f:
            xml = f.read()
    else:
        url = config['svgUrl'].format(config['style'].lower(), icon)
        print('download: ', url)
        req = request.Request(url)
        xml = request.urlopen(req, context=ssl.create_default_context(cafile=certifi.where())).read().decode()
        if not xml:
            return ''
        with open(temp, 'w+') as f:
            f.write(xml)
    return xml


def parseSVG(icon, svg):
    a = re.match(r'<svg.*?>(.*)<\/svg>', svg, re.S)
    return '<g id="{}">{}</g>'.format(icon, re.search('<svg.*?>(.*)<\/svg>', svg, re.S).groups()[0].replace('\n',''))


def generateElement(slot):
    with open(currentPath.format(config['template']), 'r') as fr:
        with open(currentPath.format(os.path.join('dist', config['elementName']+'.js')), 'w') as fw:
            fw.write(fr.read().format(slot))


if __name__ == '__main__':
    config = readJson('config.json')
    r = []
    for icon in config['icons']:
        svg = getSVG(icon)
        if svg:
            r += [parseSVG(icon, svg)]
        else:
            print('error when get icon', icon)
            break
    generateElement('\n'.join(r))
