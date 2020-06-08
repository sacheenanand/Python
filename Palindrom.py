{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is it Palindrom True\n",
      "is it Palindrom False\n",
      "is it Palindrom True\n"
     ]
    }
   ],
   "source": [
    "# palindrome program\n",
    "\n",
    "def palindrome(s):\n",
    "    head,tail=0,len(s)-1\n",
    "    while head < tail:\n",
    "        while not s[head].isalnum():\n",
    "            head+=1\n",
    "        while not s[tail].isalnum():\n",
    "            tail-=1\n",
    "        if s[head].lower()!= s[tail].lower():\n",
    "            return False\n",
    "            \n",
    "        head+=1\n",
    "        tail-=1\n",
    "    return True\n",
    "print(\"is it Palindrom\", palindrome(\"bob\"))\n",
    "        \n",
    "print(\"is it Palindrom\", palindrome(\"car\"))\n",
    "print(\"is it Palindrom\", palindrome(\"BAb\"))\n",
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
