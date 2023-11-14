#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>

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

void secret_algorithm2(uint8_t* arr, int n) {
  for (int i = n-1; i > 0; i--) {
    for (int j = n-i-1 ; j > 0; j--) {
      if (arr[j] < arr[j+1]) {
        swap(&arr[j], &arr[j+1]);
      }
    }
  }
}

int main(int argc, char *argv[])
{
  //uint8_t arr[] = { 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47 };
  uint8_t arr[] = { 0x41,0x41,0x43,0x43,0x44,0x45,0x45,0x45,0x47,0x48,0x49,0x49,0x49,0x4c,0x4c,0x4d,0x4e,0x4e,0x4e,0x4f,0x4f,0x4f,0x52,0x53,0x53,0x53,0x54 };

  secret_algorithm2(arr, 27);

  for( int i = 0; i < 27; i++)
	  printf("%02x ", arr[i]);
  printf("\n");
  return 0;
}
