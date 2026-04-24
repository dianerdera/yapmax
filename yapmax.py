import json
import random

print("welcome to yapmax :3")
print("be ready for your personality to be brutally tested >3<")
print("pick your poison"
print("1--> niche tinder: to take skill based match making to another level")
print("2--> questionable stance: hot takes, hot chicks")
print("3--> would you rathers: because the best conversations start with side eyes and icks")
print("4--> date dice: where matches stop yapping and start doing (or yap while doing)")
print("5-->idk")

ch=int(input("enter your poison"))
if ch==1:
      def load_data(filename):
          file=open(filename,"r")
          data=json.load(file)
          file.close()
          return data

      def yapmax():
          topics=load_data("topics.json")
          topic_list=list(topics.keys())
          user1=input("the baddie:")
          user2=input("the joru ka gulaam:")

          user1_likes=[]
          user2_likes=[]

          num=int(input("how many topics do you want to swipe on"))
          selected_topics=random.sample(topic_list,num)

          print(user 1,"'s chance to be honest")
          for topic in selectd_topics:
              ans=input("do you like" + topic + "? (y/n):")
              if ans.upper()="Y":
                  user1_likes.append(topic)

          print("switching..no cheating x-(")
          print("user2,"'s turn")
          for topic in selectd_topics:
              ans=input("do you like" + topic + "? (y/n):")
              if ans.upper()="Y":
                  user2_likes.append(topic)

          common=[]
          for t in user1_likes:
                if t in user2_likes:
                     common.append(t)

          print("result time *drum beatsss*")

          if len(common)>0:
                print(" start a mini podcast on")
                for c in common:
                    print(c)

          else:
              print("no common inteerests here but hey! yap about your top niches to eo anyway")

          

