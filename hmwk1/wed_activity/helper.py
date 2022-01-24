from datetime import datetime



color_codes = {'severe-storm': 'c7e9b4', 'tropical-cyclone': '081d58', 'flooding': '41b6c4', 'drought-wildfire': 'ffffd9'}

def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))


def main():
    year_prev = ''
    f = open('data.txt', 'r')
    lines = f.readlines()
    y_pos = 0
    for l in lines:
        l = l.replace('\n', '')
        if (l != ''):
            split_lines = l.split(' ')
            yr = split_lines[1].split('-')[0]
            day_num = datetime.fromisoformat(split_lines[1]).strftime("%j")
            x_pos = str(mapRange(int(day_num), 0, 365, 50, 950)).split('.')[0]
            radius = float(split_lines[2]) * 10
            color = color_codes[split_lines[0]]
            
            
            
            if (yr != year_prev or year_prev == ''):
                year_prev = yr
                y_pos = y_pos + 50
                print('<text x="0" y='+str(y_pos + 3)+ ' fill="black">'+yr+'</text>\n<line x1="50" y1="'+str(y_pos)+'" x2="950" y2="'+str(y_pos)+'" style="stroke:rgb(95, 95, 95);stroke-width:1"></line>')
                
            
            ret =  '<circle cx="'+str(x_pos)+'" cy="'+str(y_pos)+'" r="'+str(radius)+'" stroke="grey" opacity="0.6" style="fill:' + '"%23'+ color + '"/>'
            
            print(ret)
            
            

main()