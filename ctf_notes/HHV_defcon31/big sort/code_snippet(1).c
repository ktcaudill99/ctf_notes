// uint8_t arr[] = { SECRET_REDUCTED };

void swap(uint8_t *xp, uint8_t *yp) {
  uint8_t temp = *xp;
  *xp = *yp;
  *yp = temp;
  volatile int x = 1234;
  for (volatile int i = 0; i < 10; i++) {
    x = x * i;
  }
}

void secret_algorithm(uint8_t* arr, int n) {
  for (int i = 0; i < n-1; i++) {
    for (int j = 0; j < n-i-1; j++) {
      if (arr[j] > arr[j+1]) {
        swap(&arr[j], &arr[j+1]);
      }
    }
  }
}