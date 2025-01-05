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


class AuthyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "authy"

    @property
    def original_file_name(self) -> "str":
        return "authy.svg"

    @property
    def title(self) -> "str":
        return "Authy"

    @property
    def primary_color(self) -> "str":
        return "#EC1C24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Authy</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zm3.42 5.338c.274 0 .551.105.769.315l2.862
 2.862c2.054 2.039 2.084 5.35.105 7.449a.21.21 0 0
 1-.045.06l-.03.03-.03.03c-.015.015-.045.03-.06.045-2.098 1.978-5.41
 1.948-7.463-.105l-2.863-2.863a1.05 1.05 0 0 1 0-1.499 1.05 1.05 0 0 1
 1.5 0l2.861 2.863a3.23 3.23 0 0 0 4.542.03 3.244 3.244 0 0
 0-.03-4.541l-2.863-2.862a1.05 1.05 0 0 1
 0-1.5c.203-.209.472-.314.746-.314zM8.758 6.397a5.33 5.33 0 0 1 3.715
 1.564l2.863 2.862c.42.42.42 1.08 0 1.5-.42.419-1.08.419-1.5 0L10.975
 9.46a3.249 3.249 0 0 0-4.558-.015 3.243 3.243 0 0 0 .03 4.54l2.863
 2.863c.42.42.42 1.08 0 1.499a1.05 1.05 0 0 1-1.499 0L4.95
 15.484c-2.054-2.053-2.084-5.365-.105-7.463.015-.03.03-.045.045-.06l.03-.03.03-.03c.015-.015.045-.03.06-.045a5.355
 5.355 0 0 1 3.748-1.46z" />
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
