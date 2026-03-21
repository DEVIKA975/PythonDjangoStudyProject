from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def printHello(request):
    movie_data ={'movies': [{
        'title': 'Inception',
        'summary': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
        'year': 2010,
        'success': False  
    },
    {
        'title': 'The Dark Knight',
        'summary': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
        'year': 2008,
        'success': True
    },
    {
        'title': 'Interstellar',
        'summary': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'year': 2014,
        'success': True
    },
    {
        'title': 'The Matrix',
        'summary': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
        'year': 1999,
        'success': True
    },
    {
        'title': 'The Room',
        'summary': 'Johnny is a successful bank executive who lives quietly in a San Francisco townhouse with his fiancée, Lisa. One day, inexplicably, she gets bored with him and decides to seduce his best friend, Mark. From there, nothing will be the same again.',
        'year': 2003,
        'success': False
    },
    {
        'title': 'Birdemic: Shock and Terror',
        'summary': 'A horde of mutated birds attack the residents of a small town, causing widespread panic and destruction.',
        'year': 2010,
        'success': False
    },
    {
        'title': 'Plan 9 from Outer Space',
        'year': 1959,
        'success': False
    },
    {
        'title': 'Troll 2',
        'summary': '',
        'year': 1990,
        'success': False
    },
    ]}
    
    return render(request, 'hello.html', movie_data)
