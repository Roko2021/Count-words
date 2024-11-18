def count_words_in_md(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()  # تقسيم النص إلى كلمات
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"الملف '{file_path}' غير موجود.")
        return 0

# مثال على الاستخدام
file_path = 'README.md'  # استبدل هذا المسار بمسار الملف المطلوب
word_count = count_words_in_md(file_path)
print(f"عدد الكلمات في الملف: {word_count}")
