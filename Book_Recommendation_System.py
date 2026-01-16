print("===== BOOK RECOMMENDATION SYSTEM =====")

print("\nChoose Book Category:")
print("1. Indian")
print("2. Global")
print("3. Marathi")

category = input("Enter your choice (1/2/3): ")

print("\nChoose Book Genre:")
print("1. Novel")
print("2. Short Stories")
print("3. Autobiography")
print("4. Self-Help")
print("5. Motivational")
print("6. Mythology")
print("7. Historical")

genre = input("Enter your choice (1-7): ")

print("\nRecommended Books:\n")

if category == "1" and genre == "1":
    print("• The Guide – R.K. Narayan")
    print("• Godan – Munshi Premchand")
    print("• Train to Pakistan – Khushwant Singh")
    print("• Midnight’s Children – Salman Rushdie")

elif category == "1" and genre == "2":
    print("• Malgudi Days – R.K. Narayan")
    print("• Stories by Munshi Premchand")
    print("• Ruskin Bond Short Stories")
    print("• Rabindranath Tagore Stories")

elif category == "1" and genre == "3":
    print("• Wings of Fire – A.P.J Abdul Kalam")
    print("• Playing It My Way – Sachin Tendulkar")
    print("• My Experiments with Truth – M.K. Gandhi")
    print("• Unfinished – Priyanka Chopra")

elif category == "1" and genre == "4":
    print("• Atomic Habits")
    print("• The Monk Who Sold His Ferrari")
    print("• Think Like a Monk")
    print("• The Psychology of Money")

elif category == "1" and genre == "5":
    print("• You Can Win – Shiv Khera")
    print("• Believe in Yourself – Dr. Joseph Murphy")
    print("• The Magic of Thinking Big")
    print("• Life’s Amazing Secrets")

elif category == "1" and genre == "6":
    print("• Ramayana")
    print("• Mahabharata")
    print("• Shiva Trilogy – Amish")
    print("• Asura – Anand Neelakantan")

elif category == "1" and genre == "7":
    print("• Discovery of India – Jawaharlal Nehru")
    print("• India After Gandhi – Ramachandra Guha")
    print("• The Argumentative Indian – Amartya Sen")
    print("• Ancient India – R.C. Majumdar")

elif category == "2" and genre == "1":
    print("• 1984 – George Orwell")
    print("• Pride and Prejudice – Jane Austen")
    print("• The Great Gatsby")
    print("• To Kill a Mockingbird")

elif category == "2" and genre == "2":
    print("• O. Henry Short Stories")
    print("• Edgar Allan Poe Stories")
    print("• Sherlock Holmes Stories")
    print("• Anton Chekhov Stories")

elif category == "2" and genre == "3":
    print("• The Diary of a Young Girl – Anne Frank")
    print("• Long Walk to Freedom – Nelson Mandela")
    print("• Steve Jobs – Walter Isaacson")
    print("• Becoming – Michelle Obama")

elif category == "2" and genre == "4":
    print("• The 7 Habits of Highly Effective People")
    print("• How to Win Friends and Influence People")
    print("• The Power of Now")
    print("• Rich Dad Poor Dad")

elif category == "2" and genre == "5":
    print("• Awaken the Giant Within")
    print("• The Secret")
    print("• Can’t Hurt Me")
    print("• The Subtle Art of Not Giving a F*ck")

elif category == "2" and genre == "6":
    print("• Percy Jackson")
    print("• Lord of the Rings")
    print("• Harry Potter")
    print("• The Hobbit")

elif category == "2" and genre == "7":
    print("• Sapiens – Yuval Noah Harari")
    print("• Guns, Germs, and Steel")
    print("• The Silk Roads")
    print("• A People’s History of the World")

elif category == "3" and genre == "1":
    print("• Mrityunjay – Shivaji Sawant")
    print("• Kosala – Bhalchandra Nemade")
    print("• Yayati – V.S. Khandekar")
    print("• Batatyachi Chawl – P.L. Deshpande")

elif category == "3" and genre == "2":
    print("• Vyakti ani Valli – P.L. Deshpande")
    print("• Hasavyache Phuge – P.L. Deshpande")
    print("• Ek Hota Carver")
    print("• Chimanrao")

elif category == "3" and genre == "3":
    print("• Amrutvel – Acharya Atre")
    print("• Smaran Gatha – Yashwantrao Chavan")
    print("• Majhi Janmathep – Babasaheb Ambedkar")
    print("• Eka Hatyachi Kahani")

elif category == "3" and genre == "6":
    print("• Shree Ganesh Puran")
    print("• Dnyaneshwari")
    print("• Eknathi Bhagwat")
    print("• Haripath")

elif category == "3" and genre == "7":
    print("• Shivaji Kon Hota – Babasaheb Purandare")
    print("• Raja Shivchhatrapati")
    print("• Panipat – Vishwas Patil")
    print("• Sambhaji – Vishwas Patil")

else:
    print("No recommendations available for this selection.")

print("\nThank you for using the Book Recommendation System!")
print("Happy Reading 📚")
