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


class AdyenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adyen"

    @property
    def original_file_name(self) -> "str":
        return "adyen.svg"

    @property
    def title(self) -> "str":
        return "Adyen"

    @property
    def primary_color(self) -> "str":
        return "#0ABF53"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Adyen</title>
     <path d="M11.64703 9.88245v2.93377c0
 .13405.10867.24271.24272.24271h.46316V9.88245h1.76474v5.1503c0
 .46916-.38033.8495-.8495.8495H9.94303v-1.23507h2.40991v-.52942h-1.62108c-.46917
 0-.8495-.38033-.8495-.8495V9.88245h1.76467Zm-8.26124.00001c.46917 0
 .8495.38034.8495.8495v3.3858H.8495c-.46916
 0-.8495-.38033-.8495-.8495v-.94805c0-.46917.38034-.8495.8495-.8495h.91521v1.3455c0
 .13406.10867.24272.24272.24272h.46316V11.184c0-.13405-.10867-.24271-.24272-.24271l-2.16719-.00002V9.88246Zm5.79068-1.76471v6.00001H5.79068c-.46917
 0-.8495-.38033-.8495-.8495v-2.53631c0-.46917.38033-.8495.8495-.8495h.91515v2.93377c0
 .13405.10867.24271.24272.24271h.46316l.00005-4.94118h1.76471Zm9.03286
 1.76471a.8495.8495 0 0 1 .8495.8495v.94805c0
 .46917-.38033.8495-.8495.8495h-.9152v-1.3455c0-.13404-.10868-.2427-.24272-.2427h-.46317v1.8749c0
 .13406.10867.24272.24272.24272h2.16719v1.05883h-3.32511c-.46917
 0-.8495-.38033-.8495-.8495v-3.3858Zm4.94117 0c.46916 0
 .8495.38034.8495.8495v3.3858h-1.7647V11.184c-.0004-.13388-.10884-.24232-.24272-.24272h-.46316v3.1765H19.7647V9.88245Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.adyen.com/press-and-media/presski'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.adyen.com/press-and-media/presski'''

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
