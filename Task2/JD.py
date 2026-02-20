{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8b8072dc-885c-4d79-b813-398e9e309369",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a day: 4\n",
      "enter a month (in numbers): 1\n",
      "enter a year: 1700\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2341973.1057936507\n"
     ]
    }
   ],
   "source": [
    "#ask user for input\n",
    "D= float(input(\"enter a day:\"))\n",
    "M= float(input(\"enter a month (in numbers):\"))\n",
    "Y= float(input(\"enter a year:\"))\n",
    "\n",
    "#calculate the date \n",
    "JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5\n",
    "print(JD)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Anaconda3-2025.06",
   "language": "python",
   "name": "anaconda3-2025.06"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
