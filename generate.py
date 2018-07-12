#coding=utf-8
import json
import os
from urllib import request
import xmltodict
import re

style = 'Round'#'Sharp' 'Round'
svgUrl = "https://material.io/tools/icons/static/icons/{}-{}-24px.svg"
currentPath = os.path.split(os.path.realpath(__file__))[0] + os.sep + '{}'
elementName = 'klog-icon'

def readJson(inputFile):
    with open(currentPath.format(inputFile), 'r') as f:
        return json.load(f)

def getSVG(icon):
    temp = currentPath.format(os.path.join('tmp', style+'_'+icon+'.svg'))
    if os.path.exists(temp):
        with open(temp) as f:
            xml = f.read()
    else:
        url = svgUrl.format(style.lower(),icon)
        print('download: ', url)
        req = request.Request(url)
        xml = request.urlopen(req).read().decode()
        if not xml:
            return ''
        with open(temp, 'w+') as f:
            f.write(xml)
    return xmltodict.parse(xml)

def parseSVG(svg):
    for g in svg['svg']['g']:
        if re.match(style,g['@id']):
            print(icon,json.dumps(g),sep=':\n')
            if 'g' in g and isinstance(g['g'],list):
                paths = g['g']
            else:
                paths = [g['path']]
    r = '<g id="{}">'.format(icon)
    for path in paths:
        if 'path' in path:
            path = path['path']
        if '@d' in path:
            r += '<path d="{}"/>'.format(path['@d'])
    r += '</g>'
    return r

def generateElement(slot):
    with open(currentPath.format('template.html'), 'r') as fr:
        with open(currentPath.format(os.path.join('dist', elementName+'.html')), 'w') as fw:
            fw.write(fr.read().format(slot))

if __name__=='__main__':
    icons = readJson('icons.json')
    r = []
    for icon in icons:
        svg = getSVG(icon)
        if svg:
            r += [parseSVG(svg)]
        else:
            print('error when get icon', icon)
            break
    generateElement('\n'.join(r))