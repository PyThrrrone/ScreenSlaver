# For Pythonista App on IPad
import scene, ui
from PIL import Image
shadertoy_code  = '''
// Created by Alex Kluchikov viscosity klk
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
    uv=vec2(.125,.75)+(uv-vec2(.125,.5))*.003;
    float T=iTime*.1;

    vec3 c = clamp(1.-.7*vec3(
        length(uv-vec2(1.1,1)),
        length(uv-vec2(1.1,1)),
        length(uv-vec2(1.1,1))
        ),0.,1.)*2.-1.;
    vec3 c0=vec3(0);
    float w0=0.;
    const float N=5.;
    for(float i=0.;i<N;i++)
    {
        float wt=(i*i/N/N-.2)*.3;
        float wp=0.5+(i+1.)*(i+1.5)*0.000001;
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
'''
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
''' + shadertoy_code + '''
void main(void) {
    mainImage(gl_FragColor, gl_FragCoord.xy);
}
'''
class MyScene (scene.Scene):
    def setup(self):
        screen_size = ui.get_screen_size()
        self.sprite = scene.SpriteNode(
            size=screen_size,
            parent=self)
        self.sprite.shader = scene.Shader(shader_text)
        self.sprite.position = self.size/2
        
    def touch_began(self, touch):
        self.set_touch_position(touch)

    def touch_moved(self, touch):
        self.set_touch_position(touch)

    def set_touch_position(self, touch):
        dx, dy = self.sprite.position - touch.location
        self.sprite.shader.set_uniform('u_offset', (dx, dy))
        self.sprite

scene.run(MyScene(), show_fps=False, anti_alias=True, frame_interval=1)
