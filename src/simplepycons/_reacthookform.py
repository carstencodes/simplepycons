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


class ReactHookFormIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "reacthookform"

    @property
    def original_file_name(self) -> "str":
        return "reacthookform.svg"

    @property
    def title(self) -> "str":
        return "React Hook Form"

    @property
    def primary_color(self) -> "str":
        return "#EC5990"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>React Hook Form</title>
     <path d="M10.7754 17.3477H5.8065a.2815.2815 0 1 0 0
 .563h4.9689a.2815.2815 0 1 0 0-.563zm7.3195 0h-4.9688a.2815.2815 0 1
 0 0 .563h4.9688a.2815.2815 0 0 0
 0-.563zm-7.3336-6.475H5.8065a.2815.2815 0 1 0 0
 .563h4.9548a.2815.2815 0 1 0 0-.563zm7.3195 0h-4.9547a.2815.2815 0 1
 0 0 .563h4.9547a.2815.2815 0 0 0 0-.563zm.5518-9.2001h-4.341a2.4042
 2.4042 0 0 0-4.5804 0H5.3674c-1.7103 0-3.0968 1.3864-3.0968
 3.0967v16.134C2.2706 22.6135 3.6571 24 5.3674 24h13.2652c1.7103 0
 3.0968-1.3865
 3.0968-3.0967V4.7693c0-1.7103-1.3865-3.0967-3.0968-3.0967zm-8.7046.563a.2815.2815
 0 0 0 .2815-.2224 1.8411 1.8411 0 0 1 3.5979 0 .2815.2815 0 0 0
 .2815.2224h1.5146v1.844a.8446.8446 0 0 1-.8446.8446H9.2552a.8446.8446
 0 0 1-.8446-.8446v-1.844Zm11.2383 18.6677c0 1.3993-1.1344
 2.5337-2.5337 2.5337H5.3674c-1.3993
 0-2.5337-1.1344-2.5337-2.5337V4.7693c0-1.3993 1.1344-2.5337
 2.5337-2.5337h2.4802v1.844c0 .7774.6302 1.4076 1.4076
 1.4076h5.4896c.7774 0 1.4076-.6302 1.4076-1.4076v-1.844h2.4802c1.3993
 0 2.5337 1.1344 2.5337 2.5337z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/react-hook-form/documentat'''

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
