# DisneyPlus Clone Project
This is a simple project that allow users to upload their favorite movies

From the backend (django admin) to the frontend it also have google authentication

That allows users to login with thier google account.
This project [DisneyPlusCone](https://disneyhotstar.herokuapp.com/) is hosted on heroku server

For now but looks forward to update with it another free tier server since heroku will not be
using free tier's again.


## Models

```python
class BannerCards(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    imageurl = models.CharField(max_length=1000)
    targetUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Cards(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    imageurl = models.CharField(max_length=1000)
    targetUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
```

```python

def home(request):
    bannerCards = BannerCards.objects.all()
    cards = Cards.objects.all()
    context = {
        'bannerCards': bannerCards,
        'cards': cards,
    }
    return render(request, "Home/home.html", context)

def search(request):
    query = request.GET['query']
    title = Cards.objects.filter(title__icontains=query)
    category = Cards.objects.filter(category__icontains=query)
    allCards = title.union(category)
    context = {
        'allCards': allCards,
        "query": query,
    }
    return render(request, "Home/search.html", context)

def logout(request):
    auth.logout(request)
    return redirect("/")

```

### Project Setup
```
1. python3 -m venv project
2. source project/bin/activate
3. pip install -r requirements.txt
4. python3 manage.py test
5. python3 manage.py runserver
```