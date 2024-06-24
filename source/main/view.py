




class MainMenuView:

    def display_menu(self)->int:
        print("*** Ընտրեք Մենյուն***")
        print("1. Կառավարեք ծախսերը (ավելացնել,տեստնել)")
        print("2․ Տեսնել զեկույցները")
        print("3․ Ավելացնել գումար")
        selected_option = int(input("Ընտրեք Մենյուն (1 2 կամ 3) "))
        return selected_option
        