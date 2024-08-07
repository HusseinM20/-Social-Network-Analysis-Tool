from networkx import connected_components
import graph
from socialNetwork import SocialNetwork
import user
from visualisations import plot_graph
from algorithms import *


def main(self):
    network = SocialNetwork()

    while True:
        print("\nSocial Network CLI")
        print("1. Add User")
        print("2. Remove User")
        print("3. Add Friendship")
        print("4. Remove Friendship")
        print("5. Display Network")
        print("6. BFS Traversal")
        print("7. DFS Traversal")
        print("8. Dijkstra's Shortest Path")
        print("9. Connected Components")
        print("10. Sort Users")
        print("11. Search User")
        print("12. Network Statistics")
        print("13. Recommend Friends")
        print("14. Add Interest")
        print("15. Remove Interest")
        print("16. Add Post")
        print("17. Remove Post")
        print("18. Exit")

   
        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            network.add_user(user_id, name)

            while True:
                interest = input("Enter an interest (or 'done' to finish): ")
                if interest.lower() == 'done':
                    break
                user = network.users.get(user_id)
                user.add_interest(interest)

            while True:
                post = input("Enter a post (or 'done' to finish): ")
                if post.lower() == 'done':
                    break
                user.add_post(post)

        elif choice == '2':
            user_id = input("Enter user ID to remove: ")
            network.remove_user(user_id)

        elif choice == '3':
            user1_id = input("Enter first user ID: ")
            user2_id = input("Enter second user ID: ")
            network.add_friendship(user1_id, user2_id)

        elif choice == '4':
            user1_id = input("Enter first user ID: ")
            user2_id = input("Enter second user ID: ")
            network.remove_friendship(user1_id, user2_id)

        elif choice == '5':
            network.display_network()

        elif choice == '6':
            start_vertex = input("Enter starting vertex for BFS: ")
            bfs(network, start_vertex)

        elif choice == '7':
            start_vertex = input("Enter starting vertex for DFS: ")
            dfs(network, start_vertex)

        elif choice == '8':
            start_vertex = input("Enter starting vertex for Dijkstra's: ")
            distances = dijkstra(network, start_vertex)
            print(f"Distances from {start_vertex}: {distances}")

        elif choice == '9':
            components = connected_components(network)
            print(f"Connected Components: {components}")

        elif choice == '10':
            attribute = input("Enter attribute to sort by (user_id, name, number_of_friends): ")
            sorted_users = merge_sort(list(network.users.values()), attribute)
            for user in sorted_users:
                print(user)

        elif choice == '11':
            attribute = input("Enter attribute to search by (user_id, name): ")
            value = input(f"Enter value for {attribute}: ")
            found_user = binary_search_user(list(network.users.values()), attribute, value)
            if found_user:
                print(f"User found: {found_user}")
            else:
                print("User not found.")

        elif choice == '12':
            avg_friends = average_number_of_friends(network)
            density = network_density(network)
            user_id = input("Enter user ID for clustering coefficient: ")
            cluster_coeff = clustering_coefficient(network, user_id)
            print(f"Average number of friends: {avg_friends}")
            print(f"Network density: {density}")
            print(f"Clustering coefficient for {user_id}: {cluster_coeff}")

        elif choice == '13':
            user_id = input("Enter user ID for recommendations: ")
            recommendations = recommend_friends(network, user_id)
            print(f"Friend recommendations for {user_id}: {recommendations}")

        elif choice == '14':
            user_id = input("Enter user ID to add interest to: ")
            interest = input("Enter interest: ")
            user = network.users.get(user_id)
            if user:
                user.add_interest(interest)
                print(f"Interest '{interest}' added to user {user_id}.")
            else:
                print(f"User {user_id} not found.")

        
        elif choice == '15':
            user_id = input("Enter user ID to remove interest from: ")
            interest = input("Enter interest: ")
            user = network.users.get(user_id)
            if user:
                user.remove_interest(interest)
                print(f"Interest '{interest}' removed from user {user_id}.")
            else:
                print(f"User {user_id} not found.")

        elif choice == '16':
            user_id = input("Enter user ID to add post to: ")
            post = input("Enter post: ")
            user = network.users.get(user_id)
            if user:
                user.add_post(post)
                print(f"Post added to user {user_id}.")
            else:
                print(f"User {user_id} not found.")

        elif choice == '17':
            user_id = input("Enter user ID to remove post from: ")
            post = input("Enter post: ")
            user = network.users.get(user_id)
            if user:
                user.remove_post(post)
                print(f"Post removed from user {user_id}.")
            else:
                print(f"User {user_id} not found.")

        elif choice == '18':
            plot_graph(network)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

