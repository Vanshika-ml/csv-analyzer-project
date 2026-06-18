import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_csv():
    file_path=input("Enter CSV File path:")

    try:
        df = pd.read_csv(file_path)
        print("\nCSV File Loaded Successfully ✅")
        return df

    except FileNotFoundError:
        print("\nFile not found ❌")
        return None

    except Exception as e:
        print("\nError:", e)
        return None
    
def show_data(df):
    print("\n===== FIRST 5 ROWS =====")
    print(df.head())
def dataset_info(df):
    print("\n===== DATASET INFO =====")
    df.info()
def missing_values(df):
    print("\n===== MISSING VALUES =====")
    print(df.isnull().sum())
def statistics(df):
    print("\n===== STATISTICS =====")
    print(df.describe(include='all'))
def columns(df):
    print("\n===== COLUMN NAMES =====")
    print(df.columns.tolist())
def dataset_shape(df):
    print("\n======DATASET SHAPE =====")
    print(f"Rows: {df.shape[0]}")    
    print(f"Columns: {df.shape[1]}")    

def heatmap(df):
    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.empty:
        print("\nNo numeric columns found ❌")
        return

    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()
def histogram(df):
    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.empty:
        print("\nNo numeric columns found ❌")
        return

    numeric_df.hist(figsize=(12, 8))
    plt.suptitle("Histogram Charts")
    plt.show()
def boxplot(df):
    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.empty:
        print("\nNo numeric columns found ❌")
        return

    plt.figure(figsize=(10, 6))
    numeric_df.plot(kind='box')
    plt.title("Boxplot")
    plt.show()
def clean_data(df):
    cleaned_df = df.dropna()

    print("\nMissing values removed ✅")
    print("Old Shape:", df.shape)
    print("New Shape:", cleaned_df.shape)

    return cleaned_df
def remove_duplicates(df):
    old_shape = df.shape
    df = df.drop_duplicates()

    print("\nDuplicates removed ✅")
    print("Old Shape:", old_shape)
    print("New Shape:", df.shape)

    return df
def save_csv(df):
    output_name = input("\nEnter output file name: ")

    df.to_csv(output_name, index=False)

    print(f"\nCleaned CSV saved as '{output_name}' ✅")
def menu():
    print("\n========== CSV ANALYZER ==========")
    print("1. Show First 5 Rows")
    print("2. Dataset Info")
    print("3. Dataset Shape")
    print("4. Missing Values")
    print("5. Statistics")
    print("6. Show Columns")
    print("7. Correlation Heatmap")
    print("8. Histogram Charts")
    print("9. Boxplot")
    print("10. Remove Missing Values")
    print("11. Save Cleaned CSV")
    print("12. Remove Duplicates")
    print("0. Exit")
def main():

    df = load_csv()

    if df is None:
        return

    cleaned_df = df.copy()

    while True:

        menu()

        choice = input("\nEnter your choice: ")

        if choice == '1':
            show_data(cleaned_df)

        elif choice == '2':
            dataset_info(cleaned_df)

        elif choice == '3':
            dataset_shape(cleaned_df)    

        elif choice == '4':
            missing_values(cleaned_df)

        elif choice == '5':
            statistics(cleaned_df)

        elif choice == '6':
            columns(cleaned_df)

        elif choice == '7':
            heatmap(cleaned_df)

        elif choice == '8':
            histogram(cleaned_df)

        elif choice == '9':
            boxplot(cleaned_df)    

        elif choice == '10':
            cleaned_df = clean_data(cleaned_df)

        elif choice == '11':
            save_csv(cleaned_df)

        elif choice == '12':
            cleaned_df = remove_duplicates(cleaned_df)    

        elif choice == '0':
            print("\nProgram Closed ✅")
            break

        else:
            print("\nInvalid Choice ❌")
if __name__ == "__main__":
    main()