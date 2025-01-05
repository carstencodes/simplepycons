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


class CookiecutterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cookiecutter"

    @property
    def original_file_name(self) -> "str":
        return "cookiecutter.svg"

    @property
    def title(self) -> "str":
        return "Cookiecutter"

    @property
    def primary_color(self) -> "str":
        return "#D4AA00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cookiecutter</title>
     <path d="M12.806 0a12 12 0 0 0-4.512.885A12 12 0 0 0 .858
 12.978a12 12 0 0 0 9.303 10.724 12 12 0 0 0 13.021-5.656L12.817
 12l9.244-7.65A12 12 0 0 0 12.806 0zM9.218 2.143c.34-.003.701.123
 1.193.378.847.437 1.013 1.027.36
 1.277-.487.187-2.457.177-2.932-.015-.526-.212-.38-.781.32-1.24.402-.263.72-.396
 1.059-.4zm4.077 4.052a1.292 1.292 0 0 1 .022 0 1.292 1.292 0 0 1
 1.292 1.291 1.292 1.292 0 0 1-1.292 1.292 1.292 1.292 0 0
 1-1.292-1.292 1.292 1.292 0 0 1 1.27-1.291zm-6.259 3.8c1.033 0
 1.788.434 1.788 1.028 0 .694-1.961 2.384-2.766 2.384-.365
 0-.727-.166-.804-.368-.078-.203.117-.97.434-1.706.505-1.176.67-1.338
 1.348-1.338zm8.637 9.187c.372 0 1.362 2.316 1.186
 2.775-.201.524-1.046.467-1.564-.105-.676-.747-.404-2.67.378-2.67z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/cookiecutter/cookiecutter/
blob/52dd18513bbab7f0fbfcb2938c9644d9092247cf/logo/cookiecutter-logo.s'''

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
