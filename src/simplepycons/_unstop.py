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


class UnstopIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "unstop"

    @property
    def original_file_name(self) -> "str":
        return "unstop.svg"

    @property
    def title(self) -> "str":
        return "Unstop"

    @property
    def primary_color(self) -> "str":
        return "#1C4980"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Unstop</title>
     <path d="M12 0C5.394 0 0 5.394 0 12s5.394 12 12 12 12-5.394
 12-12S18.606 0 12 0Zm-1.2 16.86H8.303v-1.127c-.715 1.091-1.588
 1.552-2.897 1.552-2.085 0-3.248-1.2-3.248-3.333V7.248h2.509v6.182c0
 1.164.533 1.722 1.6 1.722 1.224 0 2.012-.752
 2.012-1.891V7.236h2.509v9.625zm8.533
 0v-5.939c0-1.14-.533-1.721-1.6-1.721-1.224 0-2.012.752-2.012
 1.89v5.77h-2.509V7.237h2.497V8.63c.715-1.09 1.588-1.551 2.897-1.551
 2.085 0 3.249 1.2 3.249 3.333v6.449z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://unstop.com/our-partners/branding-guid'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://unstop.com/our-partners/branding-guid'''

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
