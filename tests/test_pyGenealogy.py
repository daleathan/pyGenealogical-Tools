'''
Created on 13 ago. 2017

@author: Val
'''
import unittest
from datetime import date
from pyGenealogy.common_profile import gen_profile


class Test(unittest.TestCase):


    def test_introducing_gender(self):
        '''
        Testing right introduction of gender in common_profile
        '''
        profile = gen_profile("Name", "Surname")
        assert(profile.setCheckedGender("F"))
        assert(profile.setCheckedGender("M"))
        self.assertFalse(profile.setCheckedGender("J"))
    def test_introducing_birth_date(self):
        '''
        Testing right introduction of birth date in common_profile
        '''
        birth_date = date(2016,10, 20)
        birth_date_late = date(2017,12, 31)
        death_date_before_birth = date(2016,12, 31)
        batpsim_date_before_birth = date(2016,12, 31)
        profile = gen_profile("Name", "Surname")
        assert(profile.setCheckedBirthDate(birth_date, "EXACT"))
        assert(profile.setCheckedBirthDate(birth_date, "BEFORE"))
        assert(profile.setCheckedBirthDate(birth_date, "AFTER"))
        assert(profile.setCheckedBirthDate(birth_date, "ABOUT"))
        assert(not profile.setCheckedBirthDate(birth_date, "OTHER"))
        
        assert(profile.setCheckedDeathDate(batpsim_date_before_birth))
        assert(not profile.setCheckedBirthDate(birth_date_late))
        
    def test_introducing_death_date(self):
        '''
        Testing introduction of several death dates and the logic
        '''
        birth_date = date(2016,10, 20)
        death_date = date(2017,12, 31)
        death_date_before = date(2015,12, 31)
        profile = gen_profile("Name", "Surname")
        assert(profile.setCheckedDeathDate(death_date, "EXACT"))
        assert(profile.setCheckedDeathDate(death_date, "BEFORE"))
        assert(profile.setCheckedDeathDate(death_date, "AFTER"))
        assert(profile.setCheckedDeathDate(death_date, "ABOUT"))
        assert(not profile.setCheckedDeathDate(death_date, "OTHER"))
        
        assert(profile.setCheckedBirthDate(birth_date))
        assert(not profile.setCheckedDeathDate(death_date_before))
    def test_introduce_baptism_date(self):
        '''
        Testing introduction of baptism date
        '''
        birth_date = date(2016,10, 20)
        baptism_date = date(2016,12, 31)
        death_date = date(2019,12, 31)
        earliest_date = date(2015,12, 31)
        latest_date = date(2020,12, 31)
        profile = gen_profile("Name", "Surname")
        assert(profile.setCheckedBirthDate(birth_date))
        assert(profile.setCheckedDeathDate(death_date))
        assert(profile.setCheckedBaptismDate(baptism_date))
        
        assert(not profile.setCheckedBaptismDate(earliest_date))
        assert(not profile.setCheckedBaptismDate(latest_date))
        
    def test_date_check(self):
        '''
        Test of the function for date check
        '''
        profile = gen_profile("Name", "Surname")
        date1 = date(2017,1,1)
        date2 = date(2016,1,1)
        date3 = date(2015,1,1)
        date4 = date(2014,1,1)
        assert(profile.checkDateConsistency("", "","",""))
        assert(profile.checkDateConsistency(date4, "","",""))
        assert(profile.checkDateConsistency(date4, "","",date1))
        assert(profile.checkDateConsistency(date4, date3,date2,date1))
        
        assert(not profile.checkDateConsistency(date1, "","",date4))
        assert(not profile.checkDateConsistency("", date1,"",date4))
        assert(not profile.checkDateConsistency(date1, date4,"",""))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_introducing_gender']
    unittest.main()