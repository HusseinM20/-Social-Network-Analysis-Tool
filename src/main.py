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

       

if __name__ == "__main__":
    main()

