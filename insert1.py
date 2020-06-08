{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 5, 9]\n"
     ]
    }
   ],
   "source": [
    "#insertion sort\n",
    "\n",
    "list = [9, 5, 3, 2, 1]\n",
    "#[5, 9, 3, 2, 1]\n",
    "#[5, ,9,2,1]\n",
    "#[3,5,9,2,1]\n",
    "#[2,3,5,9,1]\n",
    "#[2,3,5,9,1]\n",
    "for i in range(1, len(list)):\n",
    "    temp = list[i]\n",
    "    j = i-1\n",
    "    \n",
    "    while j>=0 and list[j]>temp:\n",
    "        list[j+1] = list[j]\n",
    "        j = j-1\n",
    "    list[j+1]=temp\n",
    "print(list)\n",
    "    \n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
