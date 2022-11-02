
def call_url(url):
    print(f'{url=}')


def main():

    data = {"house": ["http//localhost:8080/1", "http//localhost:8080/2", "http//localhost:8080/3"],
            "car": ["http//localhost:8080/4", "http//localhost:8080/5", "http//localhost:8080/6"],
            "boat": ["http//localhost:8080/7", "http//localhost:8080/8", "http//localhost:8080/9"]}

    results = {'house': [], 'car': [], 'boat': []}

    for category in results.keys():
        print(f'category={category}')
        for url in data[category]:
            print(f'url={url}')
            # append pool.apply_async(call_url, args=(url, call_count))
            results[category].append(url)

    print(f'{results=}')


if __name__ == "__main__":
    main()
