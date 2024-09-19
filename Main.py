import NodesCon #type: ignore
import coord #type: ignore


if __name__ == "__main__":
    user = input("\nSelect creation method(User(U), Standard(S) or Automatic(A))\n")
    if user.lower() in ["user", "u"]:
        coord.coords_user()

    elif user.lower() in ["standars", "s"]:
        print('Size of X:')
        x= int(input())
        print('Size of Y:')
        y= int(input())
        print('Size of Z:')
        z= int(input())
        coord.standarized(x,y,z)

    elif user.lower() in ["automatic", "a"]:
        user = input("What shape?\n")
        figure = getattr(NodesCon, user, None)

        if figure:
            ver= figure()[1]
            object=NodesCon.llamarIndice(NodesCon.sacarIteraciones(NodesCon.crearCaras(NodesCon.newcubegraph())), ver)
            object_3d = coord.create_3d_object(object)
            coord.export_stl(object_3d, 'output.stl')
            print("Object created")
            
        else:
            print(f"Shape {user} not found")