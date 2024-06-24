class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailhash = set()
        for i in emails:
            local, domain = i.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            emailhash.add((local,domain))
        return len(emailhash)