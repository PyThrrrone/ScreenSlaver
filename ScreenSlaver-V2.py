#!/usr/bin/env python2
# For Pythonista App on IPad

import scene, ui, datetime
from PIL import Image
import io
import StringIO
from random import randint

shadertoy_code  = ['''
// Created by Alex Kluchikov viscosity klk
// tweaked by PyThrrrone

#define PI 3.141592654
vec2 rot(vec2 p,float a)
{
    float c=sin(a*35.83);
    float s=cos(a*35.83);
    return p*mat2(s,c,c,-s);
}
void mainImage(out vec4 o, in vec2 uv)
{
    uv/=iResolution.xy;
    uv=vec2(2.1,.5)+(uv-vec2(2.1,.5))*(.008);
    
    float T=(iTime+'''+str(randint(0,24*60*60))+'''.)*.5;

    vec3 c = clamp(1.-.58*vec3(
        length(uv-vec2(1.,1)),
        length(uv-vec2(1.,1)),
        length(uv-vec2(1.,1))
        ),0.,1.)*2.-1.;
    vec3 c0=vec3(0);
    float w0=0.;
    const float N=10.;
    for(float i=0.;i<N;i++)
    {
        float wt=(i*i/N/N-.01)*0.01;
        float wp=0.5+(i+1.)*(i+1.5)*0.001;
        float wb=.03+i/N*0.03;
    	c.zx=rot(c.zx,.8*wb+T*0.85*wt+(uv.x+.7)*3.*wp);
    	c.xy=rot(c.xy,c.z*c.x*wb+5.7+T*wt+(uv.y+1.1)*14.*wp);
    	c.yz=rot(c.yz,c.x*c.y*wb+8.4-T*0.79*wt+(uv.x+uv.y*(fract(i/2.)-0.25)*4.)*16.*wp);
    	c.zx=rot(c.zx,c.y*c.z*wb+8.6-T*0.65*wt+(uv.x+.7)*2.*wp);
    	c.xy=rot(c.xy,c.z*c.x*wb+8.7-T*wt+(uv.y+1.1)*2.*wp);
        float w=(.000005-i/N);
        c0+=c*w;
        w0+=w;
    }
    c0=c0/w0*(1.-pow(uv.y-.5,2.)*2.)*-1.2+.9;
    //c0=c0/w0*(1.-pow(uv.y-.5,2.)/1.-pow(uv.x-.5,2.)*1.5)*.98+.1;
    c0*=.5+dot(c0,vec3(1,1,1))/sqrt(3.)*.333;
    c0+=pow(length(sin(c0*PI*7.))/sqrt(7.)*1.1,25.1)*(.01+.3*c0);
	o=vec4(c0,1.0);
}
''',
'''
// Created by Alex Kluchikov viscosity klk
#define PI 3.141592654
vec2 rot(vec2 p,float a)
{
    float c=cos(a*35.83);
    float s=sin(a*35.83);
    return p*mat2(s,c,c,-s);
}
void mainImage(out vec4 o, in vec2 uv)
{
    uv/=iResolution.xx;
    uv=vec2(.125,.75)+(uv-vec2(.125,.75))*.003;
    float T=(iTime+'''+str(randint(0,24*60*60))+'''.)*.1;

    vec3 c = clamp(1.-.7*vec3(
        length(uv-vec2(1.1,.95)),
        length(uv-vec2(1.1,.95)),
        length(uv-vec2(1.1,.95))
        ),0.,1.)*2.-1.;
    vec3 c0=vec3(0);
    float w0=0.;
    const float N=8.;
    for(float i=0.;i<N;i++)
    {
        float wt=(i*i/N/N-.2)*.3;
        float wp=0.5+(i+1.)*(i+1.5)*0.01;
        float wb=.05+i/N*0.1;
    	c.zx=rot(c.zx,1.6+T*0.65*wt+(uv.x+.7)*23.*wp);
    	c.xy=rot(c.xy,c.z*c.x*wb+1.7+T*wt+(uv.y+1.1)*15.*wp);
    	c.yz=rot(c.yz,c.x*c.y*wb+2.4-T*0.79*wt+(uv.x+uv.y*(fract(i/2.)-0.25)*4.)*17.*wp);
    	c.zx=rot(c.zx,c.y*c.z*wb+1.6-T*0.65*wt+(uv.x+.7)*23.*wp);
    	c.xy=rot(c.xy,c.z*c.x*wb+1.7-T*wt+(uv.y+1.1)*15.*wp);
        float w=(1.5-i/N);
        c0+=c*w;
        w0+=w;
    }
    c0=c0/w0*2.+.5;//*(1.-pow(uv.y-.5,2.)*2.)*2.+.5;
    c0*=.5+dot(c0,vec3(1,1,1))/sqrt(3.)*.5;
    c0+=pow(length(sin(c0*PI*4.))/sqrt(3.)*1.0,20.)*(.3+.7*c0);
	o=vec4(c0,1.0);
}
''',
'''
// Created by Alex Kluchikov viscosity klk
// tweaked by PyThrrrone

#define PI 3.141592654
vec2 rot(vec2 p,float a)
{
    float c=sin(a*35.83);
    float s=cos(a*35.83);
    return p*mat2(s,c,c,-s);
}
void mainImage(out vec4 o, in vec2 uv)
{
    uv/=iResolution.xy;
    uv=vec2(.125,.75)+(uv-vec2(.125,.75))*.003;
    float T=(iTime+'''+str(randint(0,24*60*60))+'''.)*.1;

    vec3 c = clamp(1.-.7*vec3(
        length(uv-vec2(1.1,1)),
        length(uv-vec2(1.1,1)),
        length(uv-vec2(1.1,1))
        ),0.,1.)*2.-1.;
    vec3 c0=vec3(0);
    float w0=0.;
    const float N=4.5;
    for(float i=0.;i<N;i++)
    {
        float wt=(i*i/N/N-.2)*.3;
        float wp=0.5+(i+1.)*(i+1.5)*0.01;
        float wb=.05+i/N*0.12;
    	c.zx=rot(c.zx,.6*wb+T*0.65*wt+(uv.x+.7)*23.*wp);
    	c.xy=rot(c.xy,c.z*c.x*wb+1.7+T*wt+(uv.y+1.1)*15.*wp);
    	c.yz=rot(c.yz,c.x*c.y*wb+2.4-T*0.79*wt+(uv.x+uv.y*(fract(i/2.)-0.25)*4.)*17.*wp);
    	c.zx=rot(c.zx,c.y*c.z*wb+1.6-T*0.65*wt+(uv.x+.7)*23.*wp);
    	c.xy=rot(c.xy,c.z*c.x*wb+1.7-T*wt+(uv.y+1.1)*15.*wp);
        float w=(1.5-i/N);
        c0+=c*w;
        w0+=w;
    }
    c0=c0/w0*2.+.2;//*(1.-pow(uv.y-.5,2.)*2.)*2.+.5;
    c0*=.9+dot(c0,vec3(1,1,1))/sqrt(3.)*.1;
    c0+=pow(length(sin(c0*PI*3.))/sqrt(3.)*1.0,10.)*(.99+.01*c0);
	o=vec4(c0,1.0);
}
'''
]
shader_text = '''
precision highp float;
varying vec2 v_tex_coord;
uniform sampler2D u_texture;
uniform float u_time;
uniform vec2 u_sprite_size;
uniform float u_scale;
uniform vec2 u_offset;
#define iGlobalTime u_time
#define iTime u_time
#define iResolution (u_sprite_size*u_scale)
#define iMouse u_offset
#define iChannel0 u_texture
#define iChannel1 u_texture
''' + shadertoy_code[0] + '''
void main(void) {
    mainImage(gl_FragColor, gl_FragCoord.xy);
}
'''

def ui2pil(imgIn):
    # create a fake png file in memory
    memoryFile = StringIO.StringIO( imgIn.to_png() )
    # this creates the pil image, but does not read the data
    imgOut = Image.open(memoryFile)
    # this force the data to be read
    imgOut.load()
    # this releases the memory from the png file
    memoryFile.close()
    return imgOut



class MyScene (scene.Scene):
    def setup(self):
        screen_size = ui.get_screen_size()
        self.sprite = scene.SpriteNode(
            size=screen_size,
            parent=self)
        self.sprite.shader = scene.Shader(shader_text)
        self.sprite.position = screen_size/2
        self.shader_index = 0
    
    def get_shapshot(self):
        with ui.ImageContext(self.size.x, self.size.y) as context:
            '''self.draw_snapshot()'''
            return ui2pil(context.get_image())
        
    def touch_began(self, touch):
        '''print("touch began")'''

    def touch_moved(self, touch):
        '''print("touch moved")'''
        
    def touch_ended(self, touch):
        
        now = str(datetime.datetime.now())
        filename = 'Screenshot_{}.png'.format(now.replace(' ', '_'))
        #with ui.ImageContext(self.view.width, self.view.height) as ctx:
        #    self.view.draw_snapshot()
        #    pil = Image.open(io.BytesIO(ctx.get_image().to_png()))
        #    pil.save(filename, quality=100)
        l = len(shadertoy_code)
        self.shader_index = int((self.shader_index + 1) % l)
        self.shader_text = '''
precision highp float;
varying vec2 v_tex_coord;
uniform sampler2D u_texture;
uniform float u_time;
uniform vec2 u_sprite_size;
uniform float u_scale;
uniform vec2 u_offset;
#define iGlobalTime u_time
#define iTime u_time
#define iResolution (u_sprite_size*u_scale)
#define iMouse u_offset
#define iChannel0 u_texture
#define iChannel1 u_texture
''' + shadertoy_code[self.shader_index] + '''
void main(void) {
    mainImage(gl_FragColor, gl_FragCoord.xy);
}
											'''
        self.sprite.shader = scene.Shader(self.shader_text)

    def set_touch_position(self, touch):
        pass
        
    def did_change_size(self):
        self.sprite.size = ui.get_screen_size()
        self.sprite.position = self.size/2
        
        
    def update(self):
        pass
                
scene.run(MyScene(), show_fps=False, anti_alias=True, frame_interval=.5)
