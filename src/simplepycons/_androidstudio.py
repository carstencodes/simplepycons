#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class AndroidStudioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "androidstudio"

    @property
    def original_file_name(self) -> "str":
        return "androidstudio.svg"

    @property
    def title(self) -> "str":
        return "Android Studio"

    @property
    def primary_color(self) -> "str":
        return "#3DDC84"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Android Studio</title>
     <path d="M19.2693 10.3368c-.3321
 0-.6026.2705-.6026.6031v9.8324h-1.7379l-3.3355-6.9396c.476-.5387.6797-1.286.5243-2.0009a2.2862
 2.2862 0 0
 0-1.2893-1.6248v-.8124c.0121-.2871-.1426-.5787-.4043-.7407-.1391-.0825-.2884-.1234-.4402-.1234a.8478.8478
 0 0
 0-.4318.1182c-.2701.1671-.4248.4587-.4123.7662l-.0003.721c-1.0149.3668-1.6619
 1.4153-1.4867 2.5197a2.282 2.282 0 0 0 .5916 1.2103l-3.2096
 6.9064H4.0928c-1.0949-.007-1.9797-.8948-1.9832-1.9896V5.016c-.0055
 1.1024.8836 2.0006 1.9859 2.0062a2.024 2.024 0 0 0
 .1326-.0037h14.7453s2.5343-.2189 2.8619
 1.5392c-.2491.0287-.4449.2321-.4449.4889 0 .7115-.5791 1.2901-1.3028
 1.2901h-.8183zM17.222 22.5366c.2347.4837.0329 1.066-.4507
 1.3007-.1296.0629-.2666.0895-.4018.0927a.9738.9738 0 0
 1-.3194-.0455c-.024-.0078-.046-.0209-.0694-.0305a.9701.9701 0 0
 1-.2277-.1321c-.0247-.0192-.0495-.038-.0724-.0598-.0825-.0783-.1574-.1672-.21-.2757l-1.2554-2.6143-1.5585-3.2452a.7725.7725
 0 0 0-.6995-.4443h-.0024a.792.792 0 0 0-.7083.4443l-1.5109
 3.2452-1.2321 2.6464a.9722.9722 0 0
 1-.7985.5795c-.0626.0053-.1238-.0024-.185-.0087-.0344-.0036-.069-.0053-.1025-.0124-.0489-.0103-.0954-.0278-.142-.0452-.0301-.0113-.0613-.0197-.0901-.0339-.0496-.0244-.0948-.0565-.1397-.0889-.0217-.0156-.0457-.0275-.0662-.045a.9862.9862
 0 0 1-.1695-.1844.9788.9788 0 0 1-.0708-.9852l.8469-1.8223
 3.2676-7.0314a1.7964 1.7964 0 0
 1-.7072-1.1637c-.1555-.9799.5129-1.9003
 1.4928-2.0559V9.3946a.3542.3542 0 0 1 .1674-.3155.3468.3468 0 0 1
 .3541 0 .354.354 0 0 1 .1674.3155v1.159l.0129.0064a1.8028 1.8028 0 0
 1 1.2878 1.378 1.7835 1.7835 0 0 1-.6439 1.7836l3.3889 7.0507.8481
 1.7643zM12.9841 12.306c.0042-.6081-.4854-1.1044-1.0935-1.1085a1.1204
 1.1204 0 0 0-.7856.3219 1.101 1.101 0 0 0-.323.7716c-.0042.6081.4854
 1.1044 1.0935 1.1085h.0077c.6046 0 1.0967-.488 1.1009-1.0935zm-1.027
 5.2768c-.1119.0005-.2121.0632-.2571.1553l-1.4127
 3.0342h3.3733l-1.4564-3.0328a.274.274 0 0
 0-.2471-.1567zm8.1432-6.7459l-.0129-.0001h-.8177a.103.103 0 0
 0-.103.103v12.9103a.103.103 0 0 0 .0966.103h.8435c.9861-.0035
 1.7836-.804 1.7836-1.79V9.0468c0 .9887-.8014 1.7901-1.7901
 1.7901zM2.6098 5.0161v.019c.0039.816.6719 1.483 1.4874 1.4869a12.061
 12.061 0 0 1 .1309-.0034h1.1286c.1972-1.315.7607-2.525
 1.638-3.4859H4.0993c-.9266.0031-1.6971.6401-1.9191
 1.4975.2417.0355.4296.235.4296.4859zm6.3381-2.8977L7.9112.3284a.219.219
 0 0 1 0-.2189A.2384.2384 0 0 1 8.098 0a.219.219 0 0 1
 .1867.1094l1.0496 1.8158a6.4907 6.4907 0 0 1 5.3186
 0L15.696.1094a.2189.2189 0 0 1 .3734.2189l-1.0302 1.79c1.6671.9125
 2.7974 2.5439 3.0975 4.4018l-12.286-.0014c.3004-1.8572 1.4305-3.488
 3.0972-4.4003zm5.3774 2.6202a.515.515 0 0 0 .5271.5028.515.515 0 0 0
 .5151-.5151.5213.5213 0 0 0-.8885-.367.5151.5151 0 0
 0-.1537.3793zm-5.7178-.0067a.5151.5151 0 0 0 .5207.5095.5086.5086 0 0
 0 .367-.1481.5215.5215 0 1 0-.734-.7341.515.515 0 0 0-.1537.3727z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
