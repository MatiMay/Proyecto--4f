#ifdef GL_ES
precision mediump float;
#endif

/* int cantObjs;
float Objs[cantObjs]; */

uniform vec2 u_resolution;
float obj1, obj2;

float sdSphere( vec3 p, float s )
{
  return length(p)-s;
}

float sdBox2(vec3 p, vec3 b) {
    vec3 q = abs(p) - b;
    return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0);
}

float opSubtraction( float d1, float d2 ){
    return max(-d1,d2);
}

float map(vec3 p) {
    vec3 b = vec3(1.0, 1.0, 1.0); // Tamaño de el objeto1
    float obj1 = sdSphere(p - vec3(-0.8, 0.3, 0.0), float(0.9));
    float obj2 = sdBox2(p-vec3(-1.4,0.9,0.0), vec3(0.5, 0.5, 0.9));
    return opSubtraction(obj2, obj1);
}

//normal??
vec3 getNormal(vec3 p) {
    float h = 0.0001;
    vec3 n;
    n.x = map(p + vec3(h, 0, 0)) - map(p - vec3(h, 0, 0));
    n.y = map(p + vec3(0, h,0)) - map(p - vec3(0, h, 0));
    n.z = map(p + vec3(0, 0, h)) - map(p - vec3(0, 0, h));
    return normalize(n);
}

//rotacion de la camara

mat3 rotationMatrix(float angleX, float angleY) {
    float cosX = cos(angleX);
    float sinX = sin(angleX);
    float cosY = cos(angleY);
    float sinY = sin(angleY);

    mat3 rotX = mat3(
        1.0, 0.0, 0.0,
        0.0, cosX, -sinX,
        0.0, sinX, cosX
    );

    mat3 rotY = mat3(
        cosY, 0.0, sinY,
        0.0, 1.0, 0.0,
        -sinY, 0.0, cosY
    );

    return rotY * rotX;
}

void main() {
    vec2 uv = (gl_FragCoord.xy - u_resolution.xy * 0.5) / u_resolution.y;
    vec3 ro = vec3(-0.9, 0.7, 4); // Camera position

    float angleX = radians(0.0); // Rotation angle around X-axis
    float angleY = radians(0.0); // Rotation angle around Y-axis
    mat3 rot = rotationMatrix(angleX, angleY);

    vec3 rd = normalize(rot * vec3(uv, -1.3)); // Rotated camera direction


    float t = 0.0;
    for (int i = 0; i < 100; i++) {
        vec3 p = ro + t * rd;
        float d = map(p);
        if (d < 0.001) {
            vec3 n = getNormal(p);
            vec3 light_dir = normalize(vec3(0, 2, 4));
            float diff = max(dot(n, light_dir), 0.0);
            gl_FragColor = vec4(diff, diff, diff, 1.0);
            return;
        }
        t += d;
    }

    gl_FragColor = vec4(0.0, 0.1, 0.3, 1.0);
}
